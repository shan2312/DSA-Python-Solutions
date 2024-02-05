def lenOfLongSubarr (arr, n, k) :
        prefix_sum = 0
        prefix_sum_hash_map = {}
        max_length = 0
        
        for index in range(n):
            prefix_sum += arr[index]
            
            if prefix_sum == k:
                max_length = (index + 1)
                
            elif (prefix_sum - k) in prefix_sum_hash_map:
                max_length = max(max_length, index - prefix_sum_hash_map[(prefix_sum - k)])
                
            else:
                prefix_sum_hash_map[prefix_sum] = index
                
        return max_length


print(lenOfLongSubarr([-7,-11,-3,-7,4,15,-13,18,-10,-10], 10, 23))

print(lenOfLongSubarr([10, -10, 12, -12, 10000, 348], 6, 348))