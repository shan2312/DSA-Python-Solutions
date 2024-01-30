def basic_calculator_2(s):
    s = s.replace(" ", "")

    result = current_number = last_number = 0
    operation = "+"

    for index in range(len(s)):

        current_char = s[index]

        if current_char.isdigit():
            current_number = current_number * 10 + int(current_char)

        if (not current_char.isdigit()) or index == len(s) - 1:

            if operation in ["+", "-"]:
                result += last_number
                last_number = (
                    current_number if operation == "+" else -1 * current_number
                )

            elif operation == "*":
                last_number = last_number * current_number

            elif operation == "/":
                last_number = int(last_number / current_number)

            current_number = 0
            operation = current_char

    result += last_number
    return result


if __name__ == "__main__":
    print(basic_calculator_2("3 + 2*5 - 16"))
