def longestSubstringWithoutDuplication(string):
    unique_elements = set()
    window_start = 0
    max_length = 0
    max_substr_start = max_substr_end = 0
    
    for window_end in range(len(string)):
            
        if string[window_end] not in unique_elements:
            unique_elements.add(string[window_end])
            
        
        else:
            
            while string[window_end] in unique_elements:
                unique_elements.remove(string[window_start])
                window_start += 1

            unique_elements.add(string[window_end])

        if (window_end - window_start + 1) > max_length:
                max_length = window_end - window_start + 1
                max_substr_start = window_start
                max_substr_end = window_end + 1

    return string[max_substr_start:max_substr_end]
            
        
if __name__ == '__main__':
    print(longestSubstringWithoutDuplication('clementisacap'))