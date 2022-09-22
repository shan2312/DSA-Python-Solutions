import collections

def build_graph(stones):
    adj_list = [[] for _ in range(len(stones))]
    
    for index1, stone1 in enumerate(stones):
        for index2, stone2 in enumerate(stones):
            if index1 != index2:
                if stone1[0] == stone2[0] or stone1[1] == stone2[1]:
                    adj_list[index1].append(index2)
                    adj_list[index2].append(index1)
    return adj_list

def removeStones(stones):
    adj_list = build_graph(stones)          
    ROWS, COLS = len(stones), len(stones[0])
    seen = set()
    
    def get_count_of_removable_stones(stone):
        q = collections.deque([stone])
        seen.add(stone)
        count = 0
        while q:
            stone_new = q.popleft()
            count += 1
            for neighbor in adj_list[stone_new]:
                if neighbor not in seen:
                    q.append(neighbor)
                    seen.add(neighbor)
                    
        return count - 1
    
    max_count = 0
    for stone in range(len(stones)):
        if stone not in seen:
            max_count += get_count_of_removable_stones(stone)
            
    return max_count 
                    
                    