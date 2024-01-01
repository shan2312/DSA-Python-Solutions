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


def get_longest_palindromic_substring_dp(s):
     dp = [[False] * len(s) for _ in range(len(s) + 1)]

     for i in range(len(s) + 1):
          dp[i][0] = True

    for j in range(len(s) + 1):
        dp[i][0] = True

     dp[]


print(get_longest_palindromic_substring_brute_force('cbbdfoofdb'))

            