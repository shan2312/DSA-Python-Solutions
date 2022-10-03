def runLengthEncoding(string):
    present_char = ''
    present_count = 0
    encoded_list = []

    for letter in string:
        
        if present_char != letter or present_count == 9:
            encoded_list.append(str(present_count))
            encoded_list.append(present_char)
            present_char = letter
            present_count = 0

        present_count += 1

    
    encoded_list.append(str(present_count) + present_char)

    return "".join(encoded_list[1:])


if __name__ == '__main__':
    print(runLengthEncoding('AAAAAAAAAABBBBBBBBBBBBBBBBBBBBCCCCCCCC'))