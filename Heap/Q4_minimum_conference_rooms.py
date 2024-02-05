import heapq

class CountConferenceRooms:
    def __init__(self) -> None:
        pass

    def get_minimum_number_of_conference_rooms(self, intervals):
        intervals.sort()

        minimum_end_times = [intervals[0][1]]
        heapq.heapify(minimum_end_times)

        for start, end in intervals[1:]:
            minimum_end_time = minimum_end_times[0]
            if start >= minimum_end_time:
                heapq.heappop(minimum_end_times)

            heapq.heappush(minimum_end_times, end)
        what is this doing ?
            
        return len(minimum_end_times)


if __name__ == '__main__':
    count_conf = CountConferenceRooms()
    print(count_conf.get_minimum_number_of_conference_rooms([[0, 6], [3, 9], [5, 12], [14, 20], [18, 22], [19, 24], [19.5, 24]]))