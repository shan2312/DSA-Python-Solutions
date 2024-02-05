import heapq
from collections import deque



def updateMaxDeque(queue, windowEnd, k, peopleScores):
    while queue and queue[0] <= (windowEnd - k):
        queue.popleft()

    while queue and peopleScores[queue[-1]] <= peopleScores[windowEnd]:
        queue.pop()

    queue.append(windowEnd)
    return queue

def updateMinDeque(queue, windowEnd, k, peopleScores):
    while queue and queue[0] <= (windowEnd - k):
        queue.popleft()

    while queue and peopleScores[queue[-1]] >= peopleScores[windowEnd]:
        queue.pop()

    queue.append(windowEnd)
    return queue


def getMinPower(peopleScores, k):
    minPower = float('inf')
    minQueue = deque()
    maxQueue = deque()

    for index in range(len(peopleScores)):
        if index < (k - 1):
            minQueue = updateMinDeque(minQueue, index, k, peopleScores)
            maxQueue = updateMaxDeque(maxQueue, index, k, peopleScores)
            continue

        minQueue = updateMinDeque(minQueue, index, k, peopleScores)
        maxQueue = updateMaxDeque(maxQueue, index, k, peopleScores)
        power = (peopleScores[maxQueue[0]] - peopleScores[minQueue[0]])
        minPower = min(minPower, power)

    return minPower



def get_min_power(peopleScores, k):
    minHeap = []
    maxHeap = []

    left = right = 0
    minPower = float('inf')
    
    while right < len(peopleScores):
        rightValue = peopleScores[right]

        if len(minHeap) < (k - 1):
            heapq.heappush(minHeap, (rightValue, right))
            heapq.heappush(maxHeap, (-1 * rightValue, right))
            right += 1
            continue

        heapq.heappush(minHeap, (rightValue, right))
        heapq.heappush(maxHeap, (-1*rightValue, right))

        while maxHeap and maxHeap[0][1] < left:
            heapq.heappop(maxHeap)

        while minHeap and minHeap[0][1] < left:
            heapq.heappop(minHeap)

        if maxHeap and minHeap:
            power = (-1*maxHeap[0][0] - minHeap[0][0])
            minPower = min(minPower, power)

        left += 1
        right += 1

    return minPower if minPower != float('inf') else -1


print(get_min_power([6, 11, 7, 2, 8, 10], 3))
print(getMinPower([6, 11, 7, 2, 8, 10], 3))
