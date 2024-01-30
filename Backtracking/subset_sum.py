def get_subset_sum(arr):
    res = []
    def backtrack(index, sum_till_now):
        if index >= len(arr):
            res.append(sum_till_now)
            return
        
        # Do not consider index
        backtrack(index + 1, sum_till_now)

        # Consider index
        backtrack(index + 1, arr[index] + sum_till_now)
        
    backtrack(0, 0)
    return res




print(get_subset_sum([2, 4, 5]))