from math import inf
def getMaxSumGoodSubarray(nums, k):
    valToPrefixSum = {}
    prefixSum = 0
    maxSum = -inf

    for i in range(len(nums)):
        endElement = nums[i]
        firstElement1 = endElement - k
        firstElement2 = endElement + k

        if valToPrefixSum.get(nums[i], inf) > prefixSum:
            valToPrefixSum[nums[i]] = prefixSum

        prefixSum += nums[i]

        if firstElement1 in valToPrefixSum:
            maxSum = max(maxSum, prefixSum - valToPrefixSum[firstElement1])

        if firstElement2 in valToPrefixSum:
            maxSum = max(maxSum, prefixSum - valToPrefixSum[firstElement2])

    return maxSum if maxSum != -inf else 0


print(getMaxSumGoodSubarray([-1,3,2,4,5], 3))
