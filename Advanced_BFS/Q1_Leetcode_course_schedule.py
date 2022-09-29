from collections import defaultdict, deque

class Solution:
    
    def count_parents(self, numCourses, prerequisites):
        
        counts_hashmap = {node : 0 for node in range(numCourses)}
        graph = defaultdict(list)
        
        for child, parent in prerequisites:
            graph[parent].append(child)
            counts_hashmap[child] += 1
            
        return graph, counts_hashmap
    
    def findOrder(self, numCourses: int, prerequisites):
        
        graph, counts_hashmap = self.count_parents(numCourses, prerequisites)
        res = []
        queue = deque()
        
        for node in counts_hashmap:
            if counts_hashmap[node] == 0:
                queue.append(node)
                
        while queue:
            
            node = queue.popleft()
            res.append(node)
            
            for child in graph[node]:
                counts_hashmap[child] -= 1
                if counts_hashmap[child] == 0:
                    queue.append(child)
                    
        return res if len(res) == len(graph) else None