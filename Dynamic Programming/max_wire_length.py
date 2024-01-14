import math
from collections import defaultdict

def get_max_wire_length(heights):
    dp =defaultdict(int)

    def get_max_wire_length_from(index, prev):
        if (index, prev) in dp:
            return dp[(index, prev)]
        
        if index >= len(heights):
            return 0
        
        # pole at minimum
        pole_at_min = math.sqrt((1 - prev)**2 + 1) + get_max_wire_length_from(index + 1, 1)

        # pole at maximum
        pole_at_max = math.sqrt((heights[index] - prev)**2 + 1) + get_max_wire_length_from(index + 1, heights[index])

        dp[(index, prev)] = max(pole_at_max, pole_at_min)
        return dp[(index, prev)]
    
    return max(get_max_wire_length_from(1, 1), get_max_wire_length_from(1, heights[0]))


print(get_max_wire_length([3, 5, 1, 2, 1, 10]))



