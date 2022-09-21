import math
import collections
def get_max_fruits(trees):
    adj_list = [[] for _ in range(len(trees))]
    for index1, tree1 in enumerate(trees):
        for index2, tree2 in enumerate(trees):
            if index1 != index2:
                x1, y1, f1, j1 = tree1
                x2, y2, f2, j2 = tree2
                dist = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
                if j1 >= dist and j2 >= dist:
                    adj_list[index1].append(index2)
                    adj_list[index2].append(index1)
        
    visit = set()
    def bfs(tree):
        q = collections.deque([(tree, trees[tree][2])])
        visit.add(tree)
        count = 0
        while q:
            popped_tree, fruits = q.popleft()
            count += fruits
            for neighbor in adj_list[popped_tree]:
                if neighbor not in visit:
                    q.append((neighbor, trees[neighbor][2]))
                    visit.add(neighbor)
                    
        return count
        
    max_fruits = 0
    for i in range(len(trees)):
        if i not in visit:
            max_fruits = max(max_fruits, bfs(i))
        
    return max_fruits

if __name__ == "__main__":
    trees = [[2,4,2,6],[10,4,5,5], [3,8,3,6], [12 , 8, 6, 5], [1, 6, 2, 6]]
    print(get_max_fruits(trees))