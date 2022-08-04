#include <Windows.h>
#include <stdlib.h>
#include <stdio.h>
#include <iostream>
#include <string>

#include <CL/cl.h>

#include "errors.h"
#include "cilktime.h"

#include "utils.h"

using namespace std;

#define M 8
#define N 8

typedef struct _opencl_dev_info{
	cl_device_type type;
	const char* name;
	cl_uint count;
} T_opencl_dev_info;


// For now only Intel and AMD are supported
//#ifdef OPENCL_ARCH_INTEL
#define OPENCL_TARGET_PLATFORM "Intel"
//#else
//#define OPENCL_TARGET_PLATFORM "AMD Accelerated Parallel Processing"
//#endif

#define UTILIZE_OPENCL_CPU 0
#define UTILIZE_OPENCL_GPU 1
#define UTILIZE_OPENCL_ACC 2

// Error handling strategy for this example is fairly simple -- just print
// a message and terminate the application if something goes wrong
#define SIMPLE_CHECK_ERRORS(ERR)        \
	if(ERR != CL_SUCCESS)                  \
{                                      \
	cerr                                   \
	<< "OpenCL error with code " << ERR    \
	<< " happened in file " << __FILE__    \
	<< " at line " << __LINE__             \
	<< ". Exiting...\n";                   \
	exit(1);                               \
}

static char *open_cl_program =
	"__kernel void matrixAdd(						\
	__global int *A,								\
	__global int *B									\
	)												\
	{												\
	int idx_row = get_global_id(0);                 \
	int idx_col = get_global_id(1);				    \
	int col_size = get_global_size(1);			    \
	int address = idx_row*col_size + idx_col;       \
	A[address] += B[address];					    \
	return;											\
	}";


int main (int argc, const char** argv)
{
	//-----------------------------------------------------------------------
    // 1. Allocate memory and initialize host buffers
	
    const unsigned int data_size = M*N;
	int* host_buffer_A = (int*)malloc(sizeof(int) * data_size);
	int* host_buffer_B = (int*)malloc(sizeof(int) * data_size);

    
    //TODO:
    //Add code here

	init_matrix(host_buffer_A, M, N);
	init_matrix(host_buffer_B, M, N);

	//print_matrix(host_buffer_A, M, N, "host_buffer_A");
	//print_matrix(host_buffer_B, M, N, "host_buffer_B");


	// The following variable stores return codes for all OpenCL calls
	// In the code it is used with SIMPLE_CHECK_ERRORS macro
	cl_int err = CL_SUCCESS;

	//-----------------------------------------------------------------------
	// 2. Query for all available OpenCL platforms on the system

	cl_uint num_of_platforms = 0;
	// Get total number of available platforms
	err = clGetPlatformIDs(0, 0, &num_of_platforms);
	SIMPLE_CHECK_ERRORS(err);
	cout << "Number of available platforms: " << num_of_platforms << endl;

	cl_platform_id* platforms = new cl_platform_id[num_of_platforms];
	// Get IDs for all platforms
	err = clGetPlatformIDs(num_of_platforms, platforms, 0);
	SIMPLE_CHECK_ERRORS(err);

	// -----------------------------------------------------------------------
	// 3. List all platforms and select one
	// We use platform name to select needed platform

	// Default substring for platform name
	const char* required_platform_subname = OPENCL_TARGET_PLATFORM;

	cl_uint selected_platform_index = num_of_platforms;

	cout << "Platform names:\n";

	for(cl_uint i = 0; i < num_of_platforms; ++i)
	{
		// Get the length for the i-th platform name
		size_t platform_name_length = 0;
		err = clGetPlatformInfo(
			platforms[i],				/* platform */ 
			CL_PLATFORM_NAME,			/* param_name */
			NULL,						/* param_value_size */
			NULL,						/* param_value */
			&platform_name_length		/* param_value_size_ret */
			);
		SIMPLE_CHECK_ERRORS(err);

		// Get the name itself for the i-th platform
		char* platform_name = new char[platform_name_length];
		err = clGetPlatformInfo(
			platforms[i],
			CL_PLATFORM_NAME,
			platform_name_length,
			platform_name,
			NULL
			);
		SIMPLE_CHECK_ERRORS(err);

		cout << "    [" << i << "] " << platform_name;

		// Decide if this i-th platform is what we are looking for
		// We select the first one matched skipping the next one if any
		if(
			strstr(platform_name, required_platform_subname) &&
			selected_platform_index == num_of_platforms // Have not selected yet
			)
		{
			cout << " [Selected]";
			selected_platform_index = i;
			// Do not stop here, just see all available platforms
		}

		cout << endl;
		delete [] platform_name;
	}

	if(selected_platform_index == num_of_platforms)
	{
		cerr
			<< "There is no found platform with name containing \""
			<< required_platform_subname << "\" as a substring.\n";
		return 1;
	}

	cl_platform_id platform = platforms[selected_platform_index];

	// -----------------------------------------------------------------------
	// 4. Let us see how many devices of each type are provided for the
	// selected platform

	// Use the following handy array to store all device types of your interest
	// The array helps to build simple loop queries in the code below

	T_opencl_dev_info
		all_devices[] =
	{
		{ CL_DEVICE_TYPE_CPU, "CL_DEVICE_TYPE_CPU", 0 },
		{ CL_DEVICE_TYPE_GPU, "CL_DEVICE_TYPE_GPU", 0 },
		{ CL_DEVICE_TYPE_ACCELERATOR, "CL_DEVICE_TYPE_ACCELERATOR", 0 }
	};

	const int NUM_OF_DEVICE_TYPES = sizeof(all_devices)/sizeof(all_devices[0]);

	cout << "Number of devices available for each type:\n";

	// Now iterate over all device types picked above and initialize count
	for(int i = 0; i < NUM_OF_DEVICE_TYPES; ++i)
	{
		err = clGetDeviceIDs(
			platform,					/* platform */
			all_devices[i].type,		/* device_type */
			NULL,						/* num_entries */
			NULL,						/* devices */
			&all_devices[i].count		/* num_devices */
			);

		if(CL_DEVICE_NOT_FOUND == err)
		{
			// That's OK to fall here, because not all types of devices, which
			// you query for may be available for a particular system
			all_devices[i].count = 0;
			err = CL_SUCCESS;
		}

		SIMPLE_CHECK_ERRORS(err);

		cout
			<< "    " << all_devices[i].name << ": "
			<< all_devices[i].count << endl;
	}

	// -----------------------------------------------------------------------
	// 5. Get all devices IDs of specific type: GPU/CPU/ACCELERATOR
	// We are going to use the GPU, CPU, or ACCELERATOR, NOT ALL at the same time

	const unsigned int device_type = UTILIZE_OPENCL_GPU;
	cl_uint device_num = all_devices[device_type].count;
	cl_device_id *devices = (cl_device_id*)malloc(sizeof(cl_device_id)*device_num);

	err = clGetDeviceIDs(
		platform,
		all_devices[device_type].type,
		device_num,
		devices,
		&device_num
		);

	SIMPLE_CHECK_ERRORS(err);

	// -----------------------------------------------------------------------
	// 6. Create OpenCL context
	// We are going to use the GPU or CPU, NOT both

	cl_context context;
	context = clCreateContext(
		NULL,					/* properties */ 
		device_num,				/* num_devices */
		devices,				/* devices */
		NULL,					/* pfn_notify */
		NULL,					/* user_data */ 
		&err					/* errcode_ret */
		); 

	SIMPLE_CHECK_ERRORS(err);

	// -----------------------------------------------------------------------
	// 7. Create command queue(s) and add device(s)

	cl_command_queue cmd_queue;

	cmd_queue = clCreateCommandQueue(
		context,				/* context */
		*devices,				/* devices[0] */
		NULL,					/* properties */
		&err					/* errcode_ret */
		);

	SIMPLE_CHECK_ERRORS(err);

	// -----------------------------------------------------------------------
	// 8. Create memory buffers
	
    cl_mem device_buffer_A;
	cl_mem device_buffer_B;


    //TODO:
    //Add code here
	device_buffer_A = clCreateBuffer(
		context,
		CL_MEM_READ_WRITE,
		sizeof(int) * data_size,
		NULL,
		&err
	);
	SIMPLE_CHECK_ERRORS(err);
	
	device_buffer_B = clCreateBuffer(
		context,
		CL_MEM_READ_ONLY,
		sizeof(int) * data_size,
		NULL,
		&err
	);
	SIMPLE_CHECK_ERRORS(err);

	// -----------------------------------------------------------------------
	// 9. Tranfer data from the host memory to the device memory


    //TODO:
    //Add code here
	err = clEnqueueWriteBuffer(
		cmd_queue,					/* command_queue */
		device_buffer_A,			/* buffer */
		CL_TRUE,					/* blocking_write */
		0,							/* offset */
		sizeof(int) * data_size,		/* size */
		host_buffer_A,				/* ptr */
		NULL,						/* num_events_in_wait_list */
		NULL,						/* event_wait_list */
		NULL						/* event */
	); SIMPLE_CHECK_ERRORS(err);

	err = clEnqueueWriteBuffer(
		cmd_queue,
		device_buffer_B,
		CL_TRUE,
		0,
		sizeof(int) * data_size,
		host_buffer_B,
		NULL,
		NULL,
		NULL
	);

	SIMPLE_CHECK_ERRORS(err);


	// -----------------------------------------------------------------------
	// 10. Create and compile OpenCL program
    
    //TODO:
    //Modify open_cl_program kernel code

	// Create Progam object
	cl_program program = clCreateProgramWithSource(
		context,							/* context */
		1,									/* count */
		(const char**)&open_cl_program,		/* strings */
		NULL,								/* lengths */
		&err								/* errcode_ret */
		);

	// Compile Program object
	err = clBuildProgram(
		program,			/* program */
		1,					/* num_devices */
		devices,			/* device_list */
		NULL,				/* options */ 
		NULL,				/* pfn_notify */
		NULL				/* user_data */ 
		);

	SIMPLE_CHECK_ERRORS(err);

	// -----------------------------------------------------------------------
	// 11. Create kernel
    
	cl_kernel kernel = NULL;
	kernel = clCreateKernel(
		program,				/* program */
		"matrixAdd",			/* kernel_name */
		&err					/* errcode_ret */
		);

	SIMPLE_CHECK_ERRORS(err);
	
	// -----------------------------------------------------------------------
	// 12. Set kernel function argument list
    
    
    //TODO:
    //Add code here
	err = clSetKernelArg(
		kernel,					/* kernel */
		0,						/* arg_index */
		sizeof(cl_mem),			/* arg_size */
		&device_buffer_A		/* arg_value */
	);

	SIMPLE_CHECK_ERRORS(err);

	err = clSetKernelArg(
		kernel,
		1,
		sizeof(cl_mem),
		&device_buffer_B
	);

	SIMPLE_CHECK_ERRORS(err);

	
	// -----------------------------------------------------------------------	
	// 13. Define work-item and work-group


    //TODO:
    //Modify Global and local work size
	size_t n_dim = 2;
    size_t global_work_size[2] = {M, N};
    size_t local_work_size[2]= { 4 , 4 };


	// -----------------------------------------------------------------------
	// 14. Enqueue (run) the kernel(s)

	err = clEnqueueNDRangeKernel(
		cmd_queue,				/* command_queue */
		kernel,					/* kernel */
		n_dim,					/* work_dim */
		NULL,					/* global_work_offset */
		global_work_size,		/* global_work_size */
		local_work_size,		/* local_work_size, also referred to as the size of the work-group */
		NULL,					/* num_events_in_wait_list */
		NULL,					/* event_wait_list */
		NULL					/* event */
		);

	SIMPLE_CHECK_ERRORS(err);

	// -----------------------------------------------------------------------
	// 15. Get results (output buffer) from global device memory
    
    
    //TODO:
    //Add code here
	err = clEnqueueReadBuffer(
	cmd_queue,				/* command_queue */
		device_buffer_A,		/* buffer */
		CL_TRUE,				/* blocking_read */
		0,						/* offset */
		sizeof(int)* data_size,	/* size */
		host_buffer_A,			/* ptr */
		NULL,					/* num_events_in_wait_list */
		NULL,					/* event_wait_list */
		NULL					/* event */
		);

		SIMPLE_CHECK_ERRORS(err);


	
	// -----------------------------------------------------------------------
	// 16. Validate returned result

	int *test_buffer_A = (int*)malloc(sizeof(int)*data_size);
	int *test_buffer_B = (int*)malloc(sizeof(int)*data_size);

	init_matrix(test_buffer_A, M, N);
	init_matrix(test_buffer_B, M, N);

	//print_matrix(test_buffer_A, M, N, "test_buffer_A");
	//print_matrix(test_buffer_B, M, N, "test_buffer_B");
	//print_matrix(host_buffer_A, M, N, "host_buffer_A");

	matrix_addition_serial(test_buffer_A, test_buffer_B, M, N);

	if(!check_results(test_buffer_A, host_buffer_A, M, N)){
		cout << "ERROR: Invalid result!" << endl;
	}else{
		cout << "Result OK!" << endl;
	}

	// -----------------------------------------------------------------------
	// 17. Free alocated resources

	free(test_buffer_A);
	free(test_buffer_B);
	free(host_buffer_A);
	free(host_buffer_B);
	free(devices);
	delete [] platforms;

	return CL_SUCCESS;
}