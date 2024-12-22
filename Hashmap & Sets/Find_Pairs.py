def find_pairs(arr1,arr2,target):
    set_arr1 = set(arr1)
    pairs = []
    for num in arr2:
        matching_value = target - num
        if matching_value in set_arr1:
            pairs.append((matching_value,num))
    return pairs

arr1 = [1, 2, 3, 4, 5]
arr2 = [2, 4, 6, 8, 10]
target = 7

pairs = find_pairs(arr1, arr2, target)
print (pairs)