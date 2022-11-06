
class CountProvinces:
    def __init__(self) -> None:
        pass
    def get_neighbors(self, isConnected, node):
        neighbors = isConnected[node]
        
        for neighbor, is_connected in enumerate(neighbors):
                if neighbor == node or is_connected == 0:
                    continue

                yield neighbor


    def mark_province_as_visited(self, start_node, isConnected, visited):
        if start_node in visited:
            return

        visited.add(start_node)

        for neighbor in self.get_neighbors(isConnected, start_node):
            self.mark_province_as_visited(neighbor, isConnected, visited)

    def get_circle_count(self, isConnected):
        visited = set()
        count_of_provinces = 0

        for start_node in range(len(isConnected)):
            if start_node in visited:
                continue
            self.mark_province_as_visited(start_node, isConnected, visited)
            count_of_provinces += 1

        return count_of_provinces


