'''
roblem Statement:

Given a dataframe consisting of income details,

Return the name of person having the highest income.

Input Format:

A dataframe 
Output Format:

A String
Sample Input:



Sample Output:

Elon
Use the code below in order to create the given dataframe:

import pandas as pd

data = {
    'name': ['Elon', 'Jeff', 'Bill', 'Falguni'],
    'gender': ['M', 'F', 'M', 'F'],
    'income': [53000, 28000, 25000, 44000]
}

df = pd.DataFrame(data)

'''

import pandas as pd

def max_income(df):
    '''
    INPUT: df -> dataframe
    
    OUTPUT: result -> String
    
    '''
    
    ### STEP 1: Get the row with maximum income
    
    max_income = df.iloc[df['income'].idxmax()]
    
    ### STEP 2: On above result, Filter the name column and extract string value from it
    
    result = max_income['name']
    
    return result

data = {
    'name': ['Elon', 'Jeff', 'Bill', 'Falguni'],
    'gender': ['M', 'F', 'M', 'F'],
    'income': [53000, 28000, 25000, 44000]
}

df = pd.DataFrame(data)
print(max_income(df))