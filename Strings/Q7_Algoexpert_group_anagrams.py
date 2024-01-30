from collections import defaultdict

def groupAnagrams(words):
    anagram_id_to_anagram = defaultdict(list)

    for word in words:
        key = "".join(sorted(word))
        anagram_id_to_anagram[key].append(word)

    return list(anagram_id_to_anagram.values())

if __name__ == '__main__':
    print(groupAnagrams(["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]))