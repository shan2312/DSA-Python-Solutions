
from collections import defaultdict

# Solution with max_frequency optimization
# TC: O(n), SC: O(n)
def get_max_substring_length_with_same_char(s, k):
    window_start = max_substr_length = max_char_frequency = 0

    character_frequency_map = defaultdict(int)

    for window_end in range(len(s)):
        
        character_frequency_map[s[window_end]] += 1
        max_char_frequency = max(max_char_frequency, character_frequency_map[s[window_end]])

        substr_length = (window_end - window_start + 1)
        
        if (substr_length - max_char_frequency) <= k:
            max_substr_length = max(max_substr_length, substr_length) 

        else:
            while (substr_length - max_char_frequency) > k:
                character_frequency_map[s[window_start]] -= 1
                window_start += 1
                substr_length -= 1

    return max_substr_length

def get_max_substring_length_with_same_char_v2(s, k):
    window_start = max_substr_length = 0

    character_frequency_map = defaultdict(int)

    for window_end in range(len(s)):
        
        character_frequency_map[s[window_end]] += 1

        substr_length = (window_end - window_start + 1)
        
        if (substr_length - max(character_frequency_map.values())) <= k:
            max_substr_length = max(max_substr_length, substr_length) 

        else:
            while (substr_length - max(character_frequency_map.values())) > k:
                character_frequency_map[s[window_start]] -= 1
                if character_frequency_map[s[window_start]] == 0: del character_frequency_map[s[window_start]]
                window_start += 1
                substr_length -= 1

    return max_substr_length



if __name__ == '__main__':
    print(get_max_substring_length_with_same_char('AABABBA', 1))
    print(get_max_substring_length_with_same_char_v2('AABABBA', 1))
