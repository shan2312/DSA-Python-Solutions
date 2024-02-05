def get_dancing_ways(p):
    def get_dancing_ways_from(p):
        if p < 0:
            return 0 
        
        if p == 0:
            return 1
        

        a = get_dancing_ways_from(p - 1)

        
        b = (p-1)*get_dancing_ways_from(p - 2)


        return (a + b)
    
    return get_dancing_ways_from(p)

def get_dancing_ways_iterative(p):
    dp = [1]*(p + 1)


    for i in range(2, len(dp)):
        dp[i] = dp[i - 1] + (i - 1) * dp[i - 2]

    return dp[-1]



print(get_dancing_ways_iterative(5))
print(get_dancing_ways(5))


