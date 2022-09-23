from collections import deque

class Solution:
    def __init__(self):
        self.COUNT_ALPHABETS = 26
        self.START_ALPHABET_ASCII = ord('a')
        self.INITIAL_COUNT_OF_OPERATIONS = 1
        self.CANNOT_REACH_END_WORD = 0
    
    def get_neighboring_string(self, word):
        
        for pos, letter in enumerate(word):
            for ascii_offset in range(self.COUNT_ALPHABETS):
                new_letter = chr(self.START_ALPHABET_ASCII + ascii_offset)
                neighboring_word = word[:pos] + new_letter + word[(pos + 1):]
                yield neighboring_word
                
                
                
    def get_minimum_operations_to_end_word(self, beginWord, endWord, word_set):
        queue = deque([(beginWord, self.INITIAL_COUNT_OF_OPERATIONS)])
        visited = set()
        visited.add(beginWord)
        
        while queue:
            current_string, current_count_of_operations = queue.popleft()
            
            if current_string == endWord:
                return current_count_of_operations
            
            for neighbor_string in self.get_neighboring_string(current_string):
                if neighbor_string not in word_set: continue
                if neighbor_string in visited: continue
                
                queue.append((neighbor_string, current_count_of_operations + 1))
                visited.add(neighbor_string)
                
        return self.CANNOT_REACH_END_WORD
        
    
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        return self.get_minimum_operations_to_end_word(beginWord, endWord, word_set)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         """
#         BFS question
#         """
#         wordset = set(wordList)
#         q = collections.deque([(beginWord, 0)])
#         visit = set()
#         visit.add(beginWord)
        
#         while q:
#             node, depth = q.popleft()
#             if node == endWord:
#                 return depth + 1
            
#             for i in range(len(node)):
#                 for offset in range(26):
#                     temp = chr(ord('a') + offset)
#                     neighbor = node[:i] + temp + node[i + 1:]
#                     if temp != node[i] and neighbor not in visit and neighbor in wordset:
#                         q.append((neighbor, depth + 1))
#                         visit.add(neighbor)
                        
#         return 0
                        
                