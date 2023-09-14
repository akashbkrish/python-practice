'''
Given two 2D arrays, row and column ranges,

Perform the following operations:

Find the matrix multiplication of the given two matrices and
Extract the elements from the output of above step using the given ranges
If matrix multiplication is not possible, return -1
Note: The end points (upper range) of both rows and columns are excluded.

Input Format:

There will be four lines of input as follows:  
First line will have mat1.  
Second line will have mat2.  
Third line will have two space-separated integers representing start and end point of rows.  
Fourth line will have two space-separated integers representing start and end point of columns.
Output Format:

A Numpy array
Sample Input:

[[6 6 4 7 9]  
 [0 2 2 9 3]  
 [6 0 2 5 2]  
 [2 4 3 5 5]]  
[[8 6 6 8 3]  
 [2 7 0 3 1]  
 [3 2 1 5 2]  
 [7 0 7 6 8]  
 [1 5 6 4 5]]  
1 3  
2 4
Sample Output:

[[83 82]  
 [85 96]]
Sample explanation:

The dimension of product is (5,5), and the elements for rows 1 to 4 and columns 2 to 4 are prd[1][2], prd[1][3], prd[2][2] and prd[2][3] i.e. 83, 82, 85 and 96.

'''

import numpy as np
def specific_elements(mat1,mat2,r1,r2,c1,c2):
    '''mat1,mat2 are the two 2d numpy array.
       r1,r2 are the start and end of rows indices
       c1,c2 are the start and end of columns indices
       Output = Return a numpy array according to indices'''
    
    # STEP1 CHECK whether matrix multiplication is possible
    if mat1.shape[1] == mat2.shape[0]:
        
      
      ## STEP 2 Perform matrix multiplication
      
      matmul_array = np.dot(mat1,mat2)
      
      
      ## STEP 3 slice the array based on range value

      result = matmul_array[r1:r2,c1:c2]

    else:
      result = -1
    
    return result



mat1 = np.array([[6, 6, 4, 7, 9] , 
 [0, 2, 2, 9, 3], 
 [6, 0, 2, 5, 2] , 
 [2, 4, 3, 5, 5]] )

mat2 = np.array([[8, 6, 6, 8, 3],  
 [2, 7, 0, 3, 1], 
 [3, 2, 1, 5, 2],  
 [7, 0, 7, 6, 8],  
 [1, 5, 6, 4, 5]])
r1 = 1
r2 = 3
c1 = 2
c2 = 4


print(specific_elements(mat1,mat2,r1,r2,c1,c2))