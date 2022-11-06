import heapq

class KClosestPointsToOrigin:
    def __init__(self) -> None:
        pass

    def get_k_closest_points_to_origin(self, points, k):
        points_with_distance = [(-1 * (x**2 + y**2), x, y) for x, y in points]

        min_heap = points_with_distance[:k]
        heapq.heapify(min_heap)

        for negative_distance, x, y in points_with_distance[k:]:

            minimum_heap_distance = min_heap[0][0]
            if negative_distance <= minimum_heap_distance: continue
            heapq.heappop(min_heap)
            heapq.heappush(min_heap, (negative_distance, x, y))

        min_heap = [[x, y] for _, x, y in min_heap]
        return min_heap


if __name__ == '__main__':
    k_closest = KClosestPointsToOrigin()
    print(k_closest.get_k_closest_points_to_origin([[1,3],[-2,2]], 1))

            
