
START_IDX = 0

class Solution:

    def mark_rooms_as_visited(self, start_room_idx, rooms, visited):
        if start_room_idx in visited:
            return 

        visited.add(start_room_idx)
        for neighbor in rooms[start_room_idx]:
            self.mark_rooms_as_visited(neighbor, rooms, visited)


    def canVisitAllRooms(self, rooms):
        visited = set()
        self.mark_rooms_as_visited(START_IDX, rooms, visited)

        return len(visited) == len(rooms)