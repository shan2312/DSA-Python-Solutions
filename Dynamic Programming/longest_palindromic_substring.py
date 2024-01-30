# TC: O(N**3), SC: O(1)

def get_longest_palindromic_substring_brute_force(s):
    def is_palindrome(start, end):
        while start <= end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1

        return True
    
    max_len = 0
    best_i = best_j = 0

    for i in range(len(s)):
        for j in range(i, len(s)):
            this_palindrome_length = (j - i + 1)
            if is_palindrome(i, j) and this_palindrome_length > max_len:
                    max_len = this_palindrome_length
                    best_i, best_j = i, j

    return s[best_i:(best_j + 1)]


# TC: O(N**2), SC: (O(N^2))
def get_longest_palindromic_substring_dp(s):
    longest_length_string_indexes = (0, 0)
    longest_length = 0

    dp = [[False] * len(s) for _ in range(len(s))]
    
    for i in range(len(s)):
        for j in range(len(s)):
            if i < j:
                continue
            dp[i][j] = True
            if i == j:
                longest_length_string_indexes = (i, i)
                longest_length = 1

    for i in range(len(s) - 2, -1, -1):
        for j in range(i + 1, len(s)):
            dp[i][j] = (s[i] == s[j]) and dp[i + 1][j - 1]
            this_string_length = (j - i + 1)
            
            if dp[i][j] and this_string_length > longest_length:
                longest_length = this_string_length
                longest_length_string_indexes = (i, j)

    return s[longest_length_string_indexes[0] : (longest_length_string_indexes[1] + 1)]

        
def get_longest_palindromic_substring_best(s):
    longest_substring_indexes = (0, 0)
    for curent_index in range(len(s)):

        # find odd length substring
        i = j = curent_index
        while i >= 0 and j < len(s) and s[i] == s[j]:
            i -= 1
            j += 1

        longest_odd_substring_indexes = (i, j)
        odd_length = ( j - i - 1)
        
        # find even length substring
        i, j = curent_index, (curent_index + 1)
        while i >= 0 and j < len(s) and s[i] == s[j]:
            i -= 1
            j += 1

        longest_even_substring_indexes = (i, j)
        even_length = (j - i - 1)

        present_length = (longest_substring_indexes[1] - longest_substring_indexes[0] - 1)
        if present_length > max(odd_length, even_length):
            continue

        if odd_length > even_length:
            longest_substring_indexes = longest_odd_substring_indexes

        else:
            longest_substring_indexes = longest_even_substring_indexes

    return s[(longest_substring_indexes[0] + 1): longest_substring_indexes[1]]

        

        


print(get_longest_palindromic_substring_best('cbbdfoofddbkjkbdddfood'))

            