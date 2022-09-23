from collections import deque

def build_graph(bishops):
    adj_list = [[] for _ in range(len(bishops))]

    for bishop1_id, bishop1 in enumerate(bishops):
        for bishop2_id, bishop2 in enumerate(bishops):
            if bishop1_id == bishop2_id:continue

            x_one, y_one = bishop1
            x_two, y_two = bishop2

            if ((x_one - y_one) == (x_two - y_two) or (x_one + y_one) == (x_two + y_two)):
                adj_list[bishop1_id].append(bishop2_id)
                adj_list[bishop2_id].append(bishop1_id)

    return adj_list


def traverse_warring_bishops_from(start_bishop_id, seen, adj_list):
        queue = deque([start_bishop_id])
        seen.add(start_bishop_id)
        
        while queue:
            current_bishop_id = queue.popleft()
            for next_bishop_id in adj_list[current_bishop_id]:
                if next_bishop_id in seen:continue
                queue.append(next_bishop_id)
                seen.add(next_bishop_id)
        
def is_warring_bishops(bishops):
    adj_list = build_graph(bishops)
    seen = set()
                    
    traverse_warring_bishops_from(0, seen, adj_list)
    return len(seen) == len(bishops)
        
if __name__ == '__main__':
    bishops = [[6, 2], [7, 3], [8, 4], [8, 2], [3, 7]]
    print(is_warring_bishops(bishops))
