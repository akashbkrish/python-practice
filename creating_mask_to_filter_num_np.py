'''
Problem Statement:

Given an array of marks, return the array only containing elements with marks > 40
Input Format:

A 1D numpy array
Output Format:

A 1D numpy array
Sample Input:

[85, 18, 2, 57, 65, 44]
Sample Output:

[85, 57, 65, 44]
'''

import numpy as np

def filter_marks(marks):
    '''
    INPUT: marks -> 1D array
    
    OUTPUT: filtered_marks -> 1D array
    '''
    
    ### Step 1 Get the mask for marks > 40
    
    mask = marks > 40
    
    ### STEP 2 use the mask to filter the array
    
    filtered_array= marks[mask]
    
    return filtered_array

marks = np.array([85, 18, 2, 57, 65, 44])
print(filter_marks(marks))