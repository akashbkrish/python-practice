'''
Given a list of birds and their corresponding age, calculate the mean age of the Crane bird (rounded off to 2 decimal points)
Input Format:

Two 1D array list i.e. bird array and age array
Output Format:

Float value representing mean age of crane birds
Sample Input:

birds = ['spoonbills',  'plovers',  'plovers',  'plovers',  'plovers',  'Cranes',  'plovers',  'plovers',  'Cranes',  'spoonbills']
age = [5.5, 6.0, 3.5, 1.5, 3.0, 4.0, 3.5, 2.0, 5.5, 6.0]
Sample Output:

4.75
Note:

To round off the result, use np.round()
Documentation link: np.round()

'''

import numpy as np

def calculate_mean_age(birds, age):
    '''
    INPUT: birds, age -> 1D array
    
    OUPUT: mean_age -> float variable
    '''
    
    mean_age = None
    
    ## STEP1. Create mask to get Crane birds from birds array
    mask = np.where(birds=='Cranes')   # we are getting the indices where the element 'Carens' present in the birds array
     # or we can use birds=='Cranes' this work at the time
    
    ## STEP2. Get the age of crane birds
    
    crane_ages = age[mask]
    
    ## STEP 3. Calculate mean age of crane birds
    
    mean_age = np.mean(crane_ages)
    
    ## STEP 4. Round off the mean age to 2 decimal points
    
    mean_age = np.round(mean_age,2)
    
    
    
    return mean_age

birds = np.array(['spoonbills',  'plovers',  'plovers',  'plovers',  'plovers',  'Cranes',  'plovers',  'plovers',  'Cranes',  'spoonbills'])
age = np.array([5.5, 6.0, 3.5, 1.5, 3.0, 4.0, 3.5, 2.0, 5.5, 6.0])

print(calculate_mean_age(birds = birds , age = age ))