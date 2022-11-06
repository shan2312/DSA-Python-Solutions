

def insert_new_interval(intervals, newInterval):
    new_start, new_end = newInterval
    inserted_intervals = []

    for index, interval in enumerate(intervals):
        start, end  = interval

        if new_end < start:
            inserted_intervals.append([new_start, new_end])
            return inserted_intervals + intervals[index:]

        elif new_start > end:
            inserted_intervals.append(interval)

        else:
            new_start = min(start, new_start)
            new_end = max(end, new_end)

    inserted_intervals.append([new_start, new_end])
    return inserted_intervals


if __name__ == '__main__':
    print(insert_new_interval([[1,3],[6,9]], [2,5]))



