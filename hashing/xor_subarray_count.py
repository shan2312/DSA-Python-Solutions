#User function Template for python3

import math
from collections import defaultdict

class Solution:
    def subsetXOR(self, arr, N, K): 
        xor_prefix = [0 for i in range(N)]

        xor_prefix[0] = arr[0]
        
        for index in range(1, N):
            xor_prefix[index] = xor_prefix[index - 1] ^ arr[index]
            
        
        xor_counts = defaultdict(int)
        count = 0
        
        for xor_value in xor_prefix:
            complement_xor = xor_value^K
            
            if complement_xor in xor_counts:
                count += xor_counts[complement_xor]
                
            if xor_value == K:
                count += 1
                
            xor_counts[xor_value] += 1
            
        return count


s = Solution()

print(s.subsetXOR([45, 61, 77, 97], 4, 16))
print(s.subsetXOR([6, 9, 4, 2], 4, 6))