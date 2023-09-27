'''
Given a dataframe containing transaction data sorted in order of transaction date, and row range r1 (start index) and r2 (end index).

Filter out the rows between r1 and r2 (r2 is exclusive).
Complete the function select_rows() to do the same, with dataframe and r1 and r2 values provided to the function.
Return only the "name" and "amt" columns from the filtered dataframe.
Input Format:

First line of the input contains the dataframe.
Next two lines contain the value of r1 and r2 respectively.
Output Format:

The selected rows of dataframe as per r1 and r2.

Sample Input:

        date      name  amt
0 2020-01-01  Himanshu  100
1 2020-07-01    Robert  200
2 2020-08-01     Karie  400
3 2020-03-02     Rohan  150
4 2020-01-03      John  300
5 2020-10-04   Krishna  180 

r1 = 1
r2 = 3

Sample Output:

     name  amt
1  Robert  200
2   Karie  400

Sample Explanation:

We selected only rows 1 and 2, excluding 3, in the original dataset.

'''

import pandas as pd
def select_rows(df, r1, r2):
    '''
    input:
    df -> the dataframe provided to the function
    r1 -> the starting index of the rows to be selected
    r2 -> the ending index of the rows to be selected
    
    output:
    df_new -> the selected rows of the dataframe
    '''




    # Select the rows r1 to r2
    df_selected = df.loc[r1:r2-1,:]
        
    # Select the columns "name" and "amt"
    df_new = df_selected.loc[:,['name','amt']]
    
    return df_new

df = pd.DataFrame({"date": pd.to_datetime(["2020-01-01", "2020-07-01", "2020-08-01", "2020-03-02", "2020-01-03", "2020-10-04"]),
                  "name": ['Himanshu', 'Robert', 'Karie', 'Rohan', 'John', 'Krishna'],
                  "amt": [100, 200, 400, 150, 300, 180]})
r1 = 1
r2 = 3
print(df,'\n',"-----------------------","\n")
df.loc[r1:r2-1,:]
print(select_rows(df,r1,r2))