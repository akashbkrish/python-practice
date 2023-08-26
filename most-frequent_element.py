def most_frequent(arr):
    ans = None
    dict1 = dict()
    for i in range(len(arr)):
        dict1[arr[i]] = arr.count(arr[i])
    ans = max(zip(dict1.values(),dict1.keys()))[1]
    return ans

print(most_frequent([1, 3, 2, 1, 4, 1, 3]))