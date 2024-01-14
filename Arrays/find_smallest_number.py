def get_different_number(arr):
   index = 0
   while index < len(arr):
    if arr[index] >= len(arr) or arr[index] == index:
        index += 1
        continue
    temp = arr[index]
    arr[index] = arr[arr[index]]
    arr[arr[index]] = temp

    print(arr, arr[index], arr[arr[index]])
    index += 1

    print(arr)
    
    for index, num in enumerate(arr):
        if index != num:
            return index
        
    return len(arr)


print(get_different_number([2, 1, 0, 3]))