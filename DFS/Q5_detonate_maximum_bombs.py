from collections import defaultdict
import math

class CountDetonatedBombs:
    def __init__(self) -> None:
        pass

    def compute_distance(self, point_one, point_two):
        x_one, y_one = point_one
        x_two, y_two = point_two

        delta_x, delta_y = (x_one - x_two), (y_one - y_two)
        distance = math.sqrt(delta_x ** 2 + delta_y ** 2)
        return distance


    def build_graph(self, bombs):
        graph = defaultdict(list)

        for bomb_id1, bomb_info1 in enumerate(bombs):
            for bomb_id2, bomb_info2 in enumerate(bombs):

                if bomb_id1 == bomb_id2:
                    continue

                x_one, y_one, r_one = bomb_info1
                x_two, y_two, r_two = bomb_info2

                distance = self.compute_distance((x_one, y_one), (x_two, y_two))
                if distance > r_one:
                    continue

                graph[bomb_id1].append(bomb_id2)

                if distance > r_two:
                    continue

                graph[bomb_id2].append(bomb_id1)

        return graph

    def get_count_of_detonations_from(self, start_bomb_id, graph, visited):
        if start_bomb_id in visited:
            return 0

        visited.add(start_bomb_id)
        count = 1

        for neighbor in graph[start_bomb_id]:
            count += self.get_count_of_detonations_from(neighbor, graph, visited)

        return count

    
    def get_maximum_detonations(self, bombs):
        maximum_count_of_detonations = 0
        graph = self.build_graph(bombs)

        for bomb_id in range(len(bombs)):
            visited = set()
            count = self.get_count_of_detonations_from(bomb_id, graph, visited)
            maximum_count_of_detonations = max(maximum_count_of_detonations, count)

        return maximum_count_of_detonations


                