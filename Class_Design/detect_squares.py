from collections import defaultdict
from typing import List

class DetectSquares:

    def __init__(self):
        self.points_map = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.points_map[tuple(point)] += 1
        
    def count(self, point: List[int]) -> int:
        xq, yq = point
        total_count = 0
        for (x, y), count in self.points_map.items():
            if x == xq and y == yq:
                continue

            if abs(x - xq) == abs(y - yq):
                if (xq, y) not in self.points_map or (x, yq) not in self.points_map:
                    continue
                total_count += count*self.points_map[(xq, y)]*self.points_map[(x, yq)]

        return total_count
    
class DetectRectangles:

    def __init__(self):
        self.points_map = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.points_map[tuple(point)] += 1
        
    def count(self, point: List[int]) -> int:
        xq, yq = point
        total_count = 0
        print(self.points_map)
        for (x, y), count in self.points_map.items():
            if x == xq and y == yq:
                continue
            if abs(x - xq) == 0 or abs(y - yq) == 0: continue
            if (xq, y) not in self.points_map or (x, yq) not in self.points_map:
                continue
            
            total_count += count*self.points_map[(xq, y)]*self.points_map[(x, yq)]

        return total_count
    

d = DetectRectangles()
d.add([1,1])
d.add([1,4])
d.add([2,1])
d.add([2,4])
d.add([1,4])
d.add([2,1])
d.add([2,4])


print(d.count([1, 1]))

        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)