from collections import deque


def getNeighbors(word, k):
    current = word[k:]
    
    for i in range(len(word)):
        if len(word[i:(i + k)]) != k: continue
        yield current + word[i:(i + k)]
    

class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        queue = deque([word])
        minimumTime = 0
        
        while queue:
            for _ in range(len(queue)):
                print(queue)
                currentNode = queue.popleft()
                if currentNode == word and minimumTime > 0:
                    return minimumTime
                
                for neighbor in getNeighbors(currentNode, k):
                    queue.append(neighbor)
                    
            minimumTime += 1

        return minimumTime


s = Solution()
print(s.minimumTimeToInitialState('aab', 2))