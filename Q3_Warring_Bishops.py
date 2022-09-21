import collections
def is_warring_bishops(bishops):
    adj_list = [[] for _ in range(len(bishops))]
    
    for index1, bishop1 in enumerate(bishops):
        for index2, bishop2 in enumerate(bishops):
            if index1 != index2:
                x1, y1 = bishop1
                x2, y2 = bishop2
                if (x1 - y1) == (x2 - y2) or (x1 + y1) == (x2 + y2):
                    adj_list[index1].append(index2)
                    adj_list[index2].append(index1)
        
    visit = set()
    def bfs(bishop):
        q = collections.deque([bishop])
        visit.add(bishop)
        
        while q:
            bishop_popped = q.popleft()
            for neighbor in adj_list[bishop_popped]:
                if neighbor not in visit:
                    q.append(neighbor)
                    visit.add(neighbor)
                    
    bfs(0)
    return len(visit) == len(bishops)
        
if __name__ == '__main__':
    bishops = [[6, 2], [7, 3], [8, 4], [8, 2], [3, 7]]
    print(is_warring_bishops(bishops))
