from collections import defaultdict

def maximizeExpression_iterative(array):
    cache = [-1*float('inf') for _ in range(5)]
    cache[0] = 0

    for i in range(len(array) - 1, -1, -1):
        for j in range(len(cache) - 1, -1, -1):
            if (j - 1) < 0:
                continue
            sign = -1 if j%2 else 1
            cache[j] = max(cache[j], sign * array[i] + cache[j - 1])

    return cache[-1]


def maximizeExpression(array):
    cache = defaultdict(int)
    def get_max_value(index, count):
        if (index, count) in cache:
            print('DP hit')
            return cache[(index, count)]
            
        if index >= len(array):
            return 0 if count == 0 else -1*float('inf')

        sign = -1 if count%2 else 1
        a = sign * array[index] + get_max_value(index + 1, count - 1)

        b = get_max_value(index + 1, count)
        cache[(index, count)] = max(a, b)
        return cache[(index, count)]
    ans = get_max_value(0, 4) 
    return ans if ans != -1*float('inf') else 0


print(maximizeExpression_iterative([3, 6, 1, -3, 2, 7]))
