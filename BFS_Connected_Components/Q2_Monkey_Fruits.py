import math
import collections

def build_graph(trees):
    adj_list = [[] for _ in range(len(trees))]

    for tree1_id, tree1 in enumerate(trees):
        for tree2_id, tree2 in enumerate(trees):
            if tree1_id != tree2_id:
                x_one, y_one, num_fruits_one, vine_length_one = tree1
                x_two, y_two, num_fruits_two, vine_length_two = tree2
                dist = math.sqrt((x_one - x_two)**2 + (y_one - y_two)**2)
                
                if vine_length_one >= dist and vine_length_two >= dist:
                    adj_list[tree1_id].append(tree2_id)
                    adj_list[tree2_id].append(tree1_id)

    return adj_list


def get_max_fruits(trees):  
    
    adj_list = build_graph(trees) 
    seen = set()

    def get_max_reachable_fruit_from(tree_id):
        tree_fruits = trees[tree_id][2]
        q = collections.deque([(tree_id, tree_fruits)])
        seen.add(tree_id)
        total_fruits = 0

        while q:
            popped_tree_id, popped_tree_fruits = q.popleft()
            total_fruits += popped_tree_fruits

            for neighboring_tree_id in adj_list[popped_tree_id]:
                if neighboring_tree_id not in seen:
                    neighbor_fruits = trees[neighboring_tree_id][2]
                    q.append((neighboring_tree_id, neighbor_fruits))
                    seen.add(neighboring_tree_id)
                    
        return total_fruits
        
    max_reachable_fruits = 0
    for tree_id in range(len(trees)):
        if tree_id not in seen:
            max_reachable_fruits = max(max_reachable_fruits, get_max_reachable_fruit_from(tree_id))
        
    return max_reachable_fruits

if __name__ == "__main__":
    trees = [[2,4,2,6],[10,4,5,5], [3,8,3,6], [12 , 8, 6, 5], [1, 6, 2, 6]]
    print(get_max_fruits(trees))