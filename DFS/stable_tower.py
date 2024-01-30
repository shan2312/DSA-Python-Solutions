# M, N, K

def get_count_of_ways(N, M, K):
    if N == 0:
        return 1
    
    if M == 0:
        return 0
    
    count_of_ways = 0
    for k in range(K + 1):
        if N < k:
            continue
        count_of_ways += get_count_of_ways(N - k, M - 1, K)
    
    return count_of_ways



print(get_count_of_ways(3, 3, 3))
