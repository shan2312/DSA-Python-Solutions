from collections import defaultdict, Counter

def minimumCharactersForWords(words):
    max_character_frequencies = defaultdict(int) # O(S*W) space

    for word in words: # O(W*S) time
        character_frequencies = Counter(word) # O(S) space and O(S) time
        update_max_character_frequency(max_character_frequencies, character_frequencies)

    return make_array_from_character_frequencies(max_character_frequencies)

def update_max_character_frequency(max_character_frequencies, character_frequencies):
    for letter, count in character_frequencies.items():
        max_character_frequencies[letter] = max(max_character_frequencies[letter], count)

def make_array_from_character_frequencies(character_frequencies):
    character_array = []
    for character, count in character_frequencies.items():
        for i in range(count):
            character_array.append(character)

    return character_array
    
                
                
                
