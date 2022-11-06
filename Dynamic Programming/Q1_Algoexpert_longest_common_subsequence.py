
# O(m * n * min(m, n)) Space-time
def get_longest_subsequence(string1, string2):
    
    dp = [[[] for col in range(len(string2) + 1)] for row in range(len(string1) + 1)]
    
    for row in range(1, len(string1) + 1):
        for col in range(1, len(string2) + 1):

            if string1[row - 1] == string2[col - 1]:
                dp[row][col] = dp[row - 1][col - 1] + [string1[row - 1]]

            else:
                dp[row][col] = max(dp[row -1][col], dp[row][col - 1], key = len)

    return dp[-1][-1]

# O(m * n) space time
def longestCommonSubsequence(str1, str2):
    dp = [[[None, 0, None, None] for col in range(len(str2) + 1)] for row in range(len(str1) + 1)]

    for row in range(1, len(str1) + 1):
        for col in range(1, len(str2) + 1):
            
            if str1[row - 1] == str2[col - 1]:
                dp[row][col] = [str1[row - 1], 1 + dp[row - 1][col - 1][1], row - 1, col - 1]

            else:
                if dp[row - 1][col][1] > dp[row][col - 1][1]:
                    dp[row][col] = [None, dp[row - 1][col][1], row - 1, col]

                else:
                    dp[row][col] = [None, dp[row][col - 1][1], row, col - 1]

    return build_sequence(dp)

def build_sequence(dp):
    sequence = []
    i = len(dp) - 1
    j = len(dp[0]) - 1

    while i != 0 and j != 0:
        current_element = dp[i][j]
        
        if current_element[0]:
            sequence.append(current_element[0])
        i = current_element[2]
        j = current_element[3]

    return list(reversed(sequence))



if __name__ == '__main__':
    print(get_longest_subsequence("ZXVVYZW", "XKYKZPW"))

