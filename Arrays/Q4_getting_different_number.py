"""
input:  arr = [0, 1, 2, 3]

output: 4 
"""

def get_different_number_brute(arr):
    arr_set = set(arr)

    num = 0
    while True:
        if num in arr_set:
            num += 1
            continue
        return num




def get_different_number_efficient(arr):
    index = 0
    size = len(arr)

    while index < size:
        value = arr[index]
        if value == index or value >= size:
            index += 1
            continue
        arr[index], arr[value] = arr[value], arr[index]


    for index, element in enumerate(arr):
        if index != element:
            return index

    return index + 1


if __name__ == '__main__':
    print(get_different_number_brute([0, 6, 1, 2]))
    print(get_different_number_efficient([0, 6, 1, 2]))



    