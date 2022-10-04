def reverseWordsInString(string):
    string_list = list(string)
    reverse_word(string_list, 0, len(string_list) - 1)
    
    word_start = word_end = 0
    
    while word_end < len(string_list):
        
        while word_end < len(string_list) and string_list[word_end] != ' ':
            word_end += 1
            
        
        reverse_word(string_list, word_start, word_end - 1)
        
        while word_end < len(string_list) and string_list[word_end] == ' ':
            word_end += 1

        word_start = word_end

    return "".join(string_list)

def reverse_word(word, start, end):
    
    while start < end:
        word[start], word[end] = word[end], word[start]
        start += 1
        end -= 1
            

        
if __name__ == '__main__':
    print(reverseWordsInString("Tim     is Great!"))