

def get_longest_palindromic_substring(string):
    current_largest = [0, 0]

    for i in range(len(string)):
        odd = get_longest_palindrome_from(string, i, i)
        even = get_longest_palindrome_from(string, i - 1, i)

        longest = max(odd, even, key = lambda x: (x[1] - x[0] + 1))
        current_largest = max(current_largest, longest, key = lambda x : (x[1] - x[0] + 1))

    return string[current_largest[0]:current_largest[1] + 1]


def get_longest_palindrome_from(string, left, right):
    
    while left >= 0 and right < len(string) and string[left] == string[right]:
        left -= 1
        right += 1

    return [left + 1, right - 1]


if __name__ == '__main__':
    print(get_longest_palindromic_substring('abaxyzzyxf'))

