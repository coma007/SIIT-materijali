__kernel void vectorAdd(__global int *A, __global int *B, __global int *C)											
{													
	int idx = get_global_id(0);						
													
	/* Add elemets from vector A and vector B */	
	/* and store resutls to vector C */				
													
	C[idx] = A[idx] + B[idx];						
	return;											
}