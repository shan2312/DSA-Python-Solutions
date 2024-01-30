import heapq
from collections import Counter

class TopKFrequentElements:
    def __init__(self) -> None:
        pass

    def get_topk_frequent_elements(self, nums, k):
        nums = list(Counter(nums).items())
        minheap = [[frequency, num] for num,frequency in nums[:k]]
        heapq.heapify(minheap)

        for num, frequency in nums[k:]:
            min_frequency_till_now = minheap[0][0]
            if frequency > min_frequency_till_now:
                heapq.heappop(minheap)
                heapq.heappush(minheap, [frequency, num])

        return [num for _, num in minheap]


if __name__ == '__main__':
    topk = TopKFrequentElements()
    print(topk.get_topk_frequent_elements([1, 1, 1, 2, 2, 3], 2))


