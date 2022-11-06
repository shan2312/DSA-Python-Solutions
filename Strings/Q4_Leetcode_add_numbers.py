# Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

# You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.


# Input: num1 = "11", num2 = "123"
# Output: "134"

# Input: num1 = "956", num2 = "77"
# Output: "533"


def add_two_numbers_represented_as_strings(num1, num2):
    num1 = num1[::-1]
    num2 = num2[::-1]

    i = j = carry = 0
    result_list = []

    while i < len(num1) or j < len(num2):

        num1_digit = int(num1[i]) if i < len(num1) else 0
        num2_digit = int(num2[j]) if j < len(num2) else 0

        i += 1
        j += 1

        digit = num1_digit + num2_digit + carry

        carry = digit // 10
        digit = digit % 10
        
        result_list.append(str(digit))
    
    if carry > 0:
        result_list.append(str(carry))
    
    result_list.reverse()

    return "".join(result_list)


if __name__ == '__main__':
    print(add_two_numbers_represented_as_strings('123', '95'))
