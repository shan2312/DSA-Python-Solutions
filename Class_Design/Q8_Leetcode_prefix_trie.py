
class Trie:
    def __init__(self) -> None:
        self.trie = {}
        self.end_symbol = '*'

    def insert(self, word):
        curr_position = self.trie

        for char in word:
            if char not in curr_position:
                curr_position[char] = {}

            curr_position = curr_position[char]

        curr_position[self.end_symbol] = True

    def search(self, word):
        curr_position = self.trie

        for char in word:
            if char not in curr_position:
                return False

            curr_position = curr_position[char]

        return self.end_symbol in curr_position

    def startsWith(self, prefix):
        curr_position = self.trie

        for char in prefix:
            if char not in curr_position:
                return False

            curr_position = curr_position[char]

        return True



