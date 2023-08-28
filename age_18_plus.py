'''
Given a list ids that consists of special ids for a number of guests. These ids are in the form of strings where the first character is "F/M" representing their gender, the next four characters represent their year of birth and the remaining characters represent their name.

Complete the code to return a list of strings ('You can Enter' or 'No Entry for you') for each individual guest in the list according to their age.

Note: One is allowed to enter the club only if his/her age is greater than 18, considering 2022 as the present year.

For example:

ids => ['M2004Sam', 'F2001Riya', 'M1998Ani', 'F2005Diya']

Output => ['No Entry for you', 'You can Enter', 'You can Enter', 'No Entry for you']
'''

def club_entry(ids):
  age_list = [2022 - int(string[1:5]) for string in ids] #blank1
  entry = []
  for i in age_list:         
    if i >18:                #blank2                
      entry.append('You can Enter')
    else:
      entry.append('No Entry for you')
  return entry

output = club_entry(ids=['M2004Sam', 'F2001Riya', 'M1998Ani', 'F2005Diya'])
print(output)

