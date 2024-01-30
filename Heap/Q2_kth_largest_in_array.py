import heapq

class KthLargestElement:
    def __init__(self) -> None:
        pass

    def find_kth_largest_heaps(self, nums, k):
        min_heap = nums[:k]
        heapq.heapify(min_heap)

        for num in nums[k:]:
            minimum_in_heap = min_heap[0]
            
            if num > minimum_in_heap:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, num)

        return min_heap[0]



if __name__ == '__main__':
    kth_largest = KthLargestElement()
    print(kth_largest.find_kth_largest_heaps([1,2,3,4,5,6], 1))