
def get_longest_span_length(array1, array2, n):
    prefix_sum1 = prefix_sum2 = 0
    max_length = 0
    hashmap = {}

    for index in range(n):
        prefix_sum1 += array1[index]
        prefix_sum2 += array2[index]

        current_diff = (prefix_sum1 - prefix_sum2)
        if current_diff == 0:
            max_length = (index + 1)

        elif current_diff in hashmap:
            max_length = max(max_length, index - hashmap[current_diff])

        else:
            hashmap[current_diff] = index

    return max_length


print(get_longest_span_length([0, 1, 0, 0, 0, 0], [1, 0, 1, 0, 0, 1], 6))