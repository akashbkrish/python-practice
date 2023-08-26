def replace_cube(lst, N):
    new_lst = []
    
    for i in range(len(lst)):
        if (i + 1) % N == 0:
            new_lst.append(lst[i] ** 3)
        else:
            new_lst.append(lst[i])
    
    return new_lst

# Example usage
original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
N_value = 3
updated_list = replace_cube(original_list, N_value)
print(updated_list)
