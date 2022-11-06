import heapq

class MedianFinder:

    def __init__(self):
        self.lower_half = []
        self.higher_half = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.lower_half, -1 * num)

        lower_half_max_value = -1 * heapq.heappop(self.lower_half)
        heapq.heappush(self.higher_half, lower_half_max_value)

        is_median_in_higher_half = len(self.lower_half) < len(self.higher_half)

        if not is_median_in_higher_half:
            return

        higher_half_min_value = heapq.heappop(self.higher_half)
        heapq.heappush(self.lower_half, -1 * higher_half_min_value)

    def findMedian(self) -> float:
        lower_half_max_value = -self.lower_half[0] if len(self.lower_half) > 0 else None
        higher_half_min_value = self.higher_half[0] if len(self.higher_half) > 0 else None

        lower_half_has_median = len(self.lower_half) > len(self.higher_half)

        if lower_half_has_median:
            return lower_half_max_value

        return (higher_half_min_value + lower_half_max_value) / 2
        
