__kernel void matrixAdd(__global int *A, __global int *B)												{												
	int idx_row = get_global_id(0);				
	int idx_col = get_global_id(1);				
	int col_size = get_global_size(1);			
	int address = idx_row*col_size + idx_col;	
	A[address] += B[address];					
	return;										
};