# Input: heights = [4,2,3,1]
# Output: [0,2,3]
# Explanation: Building 1 (0-indexed) does not have an ocean view because building 2 is taller.

# Input: heights = [4,3,2,1]
# Output: [0,1,2,3]

# Input: heights = [1,3,2,4]
# Output: [3]


def get_ocean_view_building_indexes(heights):
    stack = []

    for building_id, building_height in enumerate(heights):
        while stack and heights[stack[-1]] <= building_height:
            stack.pop()
        stack.append(building_id)

    return stack


if __name__ == "__main__":
    print(get_ocean_view_building_indexes([4, 2, 3, 1]))
    print(get_ocean_view_building_indexes([2, 2, 2, 2]))
