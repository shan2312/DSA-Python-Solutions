def maxPoints(X, Y, N):
        hashmap = {}
        
        for index1 in range(N):
            for index2 in range(index1 + 1, N):
                slope = (Y[index1] - Y[index2])/(X[index1] - X[index2])
                
                if slope not in hashmap:
                    hashmap[slope] = 0
                hashmap[slope] += 1
                
        return max(hashmap.values())



print(maxPoints([1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], 6))