'''
Given a list of birds and their corresponding age, return the name of birds sorted according to age (ascending)
Input Format:

Two 1D array list i.e. bird array and age array
Output Format:

A 1D array
Sample Input:

birds = ['spoonbills',  'plovers',  'plovers',  'plovers',  'plovers',  'Cranes',  'plovers',  'plovers',  'Cranes',  'spoonbills']
age = [5.5, 6.0, 3.5, 1.5, 3.0, 4.0, 3.5, 2.0, 5.5, 6.0]
Sample Output:

['plovers', 'plovers', 'plovers', 'plovers', 'plovers', 'Cranes', 'spoonbills', 'Cranes', 'plovers', 'spoonbills']
Side Note: Recall the functionality of .sort() and .argsort()

'''

import numpy as np

def sort_birds(birds, age):
    '''
    INPUT: birds, age -> 1D numpy array
    
    OUTPUT: result -> sorted bird 1D array
    '''
    
    ## STEP 1 : Get the sorted index of age.
    #print(age,'\n')
    sorted_age_index = np.argsort(age)
    #print(sorted_age_index)
    
    ## STEP 2: Use the index from previous step to get sorted birds
    
    result = birds[sorted_age_index]
    #print(result)
    
    return result

birds = np.array(['spoonbills',  'plovers',  'plovers',  'plovers',  'plovers',  'Cranes',  'plovers',  'plovers',  'Cranes',  'spoonbills'])
age = np.array([5.5, 6.0, 3.5, 1.5, 3.0, 4.0, 3.5, 2.0, 5.5, 6.0])


print(sort_birds(birds, age))