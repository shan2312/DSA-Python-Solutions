# Input: intervals = [[0,30],[5,10],[15,20]]
# Output: 2
# Example 2:

# Input: intervals = [[7,10],[2,4]]
# Output: 1


import heapq

def get_minimum_number_of_conference_rooms(intervals):
    intervals.sort()

    min_heap = [intervals[0][1]]
    heapq.heapify(min_heap)

    for start_time, end_time in intervals[1:]:
        last_meeting_time = min_heap[0]
        
        if last_meeting_time <= start_time:
            heapq.heappop(min_heap)
        
        heapq.heappush(min_heap, end_time)

    return len(min_heap)


if __name__ == '__main__':
    print(get_minimum_number_of_conference_rooms([[0,30],[5,10],[15,20]]))
    print(get_minimum_number_of_conference_rooms([[7,10],[2,4]]))

