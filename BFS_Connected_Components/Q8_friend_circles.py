import collections
def build_graph(grid):
    N = len(grid)
    adj_list = [[] for i in range(N)]
    for r in range(N):
        for c in range(N):
            if r != c and grid[r][c] == 1:
                adj_list[r].append(c)
                adj_list[c].append(r)
    return adj_list

def get_friend_circles_count(grid):
    N = len(grid)
    seen = set()
    adj_list = build_graph(grid)

    def traverse_friend_circle(person):
        q = collections.deque([person])
        seen.add(person)

        while q:
            popped_person = q.popleft()
            for friend in adj_list[popped_person]:
                if friend not in seen and grid[popped_person][friend] == 1:
                    q.append(friend)
                    seen.add(friend)

    count = 0
    for r in range(N):
        if r not in seen:
            traverse_friend_circle(r)
            count += 1
    return count
                
