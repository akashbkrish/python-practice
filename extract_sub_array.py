'''Given a 2d array, write a program to return a subarray such that the subarray consists of the elements from:

1. the second to the fourth row of the original array,

2. the elements in these rows should be from the last three columns of the corresponding rows of the original array,

3. the rows should be in reversed order.

Sample Input:

[[ 0,  1,  2,  3],  
 [ 4,  5,  6,  7],   
 [ 8,  9, 10, 11],   
 [12, 13, 14, 15],   
 [16, 17, 18, 19]]
Sample Output:

array([[13, 14, 15],  
       [ 9, 10, 11], 
       [ 5,  6,  7]])
Input Format:

A 2D list
Output Format:

A 2D numpy array
Note:

This question can be solved using negative indexing and slicing'''


import numpy as np


def extract_subarray(arr):
    '''
    INPUT: arr -> 2D array
    
    OUPUT: result -> 2D array
    '''
    
    ### STEP1: Get the rows (2nd  to 4th row)
    
    row_array = arr[1:4]
    #print(row_array)
    
    
    #### STEP 2: Get the last 3 cols from the row array
    
    cols_array = row_array[:,-3:]
    
    #### STEP3: Reverse the rows in cols array
    
    result = cols_array[::-1]
    

    return result
a= np.array([[ 0,  1,  2,  3],  
            [ 4,  5,  6,  7],   
            [ 8,  9, 10, 11],   
            [12, 13, 14, 15],   
            [16, 17, 18, 19]])

print(extract_subarray(a))