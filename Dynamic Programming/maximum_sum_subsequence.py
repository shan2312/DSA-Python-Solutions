from collections import defaultdict

def get_max_sum_increasing_subsequence(array):
    dp = [[-1]*(len(array) + 1) for _ in range(len(array) + 1)]

    def dfs(index, last_index):  
        if dp[index][last_index] != -1:
            return dp[index][last_index]     
        
        if index >= len(array):
            return 0
        last_value = array[last_index]
        a = -1 * float('inf')
        if array[index] > last_value:
            a = array[index] + dfs(index + 1, array[index])

        b = dfs(index + 1, last_value)
        dp[index][last_index] = max(a, b)
        return dp[index][last_index]
    ans = dfs(0, 0)

    print(dp)
    
    return ans


def get_max_sum_increasing_subsequence2(array):
    max_path = [None]
    max_sum = -float('inf')

    def dfs(index, last_value, current_path):   
        nonlocal max_sum

        if index >= len(array):
            if sum(current_path) > max_sum:
                max_sum = sum(current_path)
                max_path.pop()
                max_path.append(current_path[:])
            return sum(current_path)
        
        a = -1 * float('inf')
        if array[index] > last_value:
            current_path.append(array[index])
            a = dfs(index + 1, array[index], current_path)
            current_path.pop()

        b = dfs(index + 1, last_value, current_path)
        
        return max(a, b)

    ans = dfs(0, -float('inf'), [])
    
    return ans, max_path[0]


def get_max_sum_iterative(array):
    pass

print(get_max_sum_increasing_subsequence([10, 70, 20, 30, 50, 11, 30, 11]))
print(get_max_sum_increasing_subsequence([3, 4, 5, 10]))
print(get_max_sum_increasing_subsequence([10, 5, 4, 3]))
print(get_max_sum_increasing_subsequence([1, 101, 2, 3, 100, 4, 5]))




print(get_max_sum_increasing_subsequence2([10, 70, 20, 30, 50, 11, 30, 11]))
print(get_max_sum_increasing_subsequence2([3, 4, 5, 10]))
print(get_max_sum_increasing_subsequence2([10, 5, 4, 3]))
print(get_max_sum_increasing_subsequence2([1, 101, 2, 3, 100, 4, 5]))


get_max_sum_increasing_subsequence2