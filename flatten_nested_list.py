def flatten(nested_list):
    flat_list = []
    
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(flatten(item))
        else:
            flat_list.append(item)
    
    return sorted(flat_list)

# Example usage
input_list = [10, [40, 20], 30, 50]
output_list = flatten(input_list)
print(output_list)


