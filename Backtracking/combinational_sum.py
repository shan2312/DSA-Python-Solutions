def get_combinational_sum(arr, x):
    res = []

    def get_combination_with_sum_k(start_index, k, combination_till_now):
        if start_index >= len(arr) or k < 0:
            return
        
        if k == 0:
            res.append(combination_till_now[:])
            return

        # Consider index
        combination_till_now.append(arr[start_index])
        get_combination_with_sum_k(start_index, k - arr[start_index], combination_till_now)
        combination_till_now.pop()

        # Do not Consider index
        get_combination_with_sum_k(start_index + 1, k, combination_till_now)

    get_combination_with_sum_k(0, x, [])
    return res



print(get_combinational_sum([2, 4, 6, 8], 8))