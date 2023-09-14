'''
Given an array in form of a matrix of size (n, n), rotate the matrix clockwise by 90º.

Input Format:

A 2d numpy array
Output Format:

A 2d numpy array
Sample Input:

[[1 2 3] 
 [4 5 6]
 [7 8 9]]
Sample Output:

[[7 4 1]
 [8 5 2]
 [9 6 3]]
Note: Try Transpose / reversing.
'''
import numpy as np
def rotate_img(mat):
    '''mat -> A 2d numpy array
       output -> A 2d numpy array is expected to be returned'''
    rotate = np.rot90(mat,3)
    '''
        transpose = mat.T                # another method
        reverse = transpose[:, ::-1]
    '''
    return rotate


mat =np.array([[1, 2, 3],  [4, 5, 6], [7, 8, 9]])
print(rotate_img(mat))