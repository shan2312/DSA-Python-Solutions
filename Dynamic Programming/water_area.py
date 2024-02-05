def waterArea(heights):
    if len(heights) == 0:
        return 0

    left_index, right_index = 0, (len(heights) - 1)
    left_max, right_max = heights[left_index], heights[right_index]
    water_area = 0
    
    while left_index < right_index:
        if heights[left_index] < heights[right_index]:
            left_index += 1
            left_max = max(left_max, heights[left_index])
            water_area += (left_max - heights[left_index])

        else:
            right_index -= 1 
            right_max = max(right_max, heights[right_index])
            water_area += (right_max - heights[right_index])

    return water_area
            