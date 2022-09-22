import collections

def build_graph(bishops):
    adj_list = [[] for _ in range(len(bishops))]

    for bishop1_id, bishop1 in enumerate(bishops):
        for bishop2_id, bishop2 in enumerate(bishops):
            if bishop1_id != bishop2_id:
                x_one, y_one = bishop1
                x_two, y_two = bishop2
                if (x_one - y_one) == (x_two - y_two) or (x_one + y_one) == (x_two + y_two):
                    adj_list[bishop1_id].append(bishop2_id)
                    adj_list[bishop2_id].append(bishop1_id)

    return adj_list
        
def is_warring_bishops(bishops):
    adj_list = build_graph(bishops)
    seen = set()

    def traverse_warring_bishops_from(bishop_id):
        q = collections.deque([bishop_id])
        seen.add(bishop_id)
        
        while q:
            popped_bishop_id = q.popleft()
            for neighboring_bishop_id in adj_list[popped_bishop_id]:
                if neighboring_bishop_id not in seen:
                    q.append(neighboring_bishop_id)
                    seen.add(neighboring_bishop_id)
                    
    traverse_warring_bishops_from(0)
    return len(seen) == len(bishops)
        
if __name__ == '__main__':
    bishops = [[6, 2], [7, 3], [8, 4], [8, 2], [3, 7]]
    print(is_warring_bishops(bishops))
