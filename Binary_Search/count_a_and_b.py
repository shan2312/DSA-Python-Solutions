def SearchPartitionStart(s):
    left, right = 0, len(s) - 1
    leftLetter = s[left]

    while left <= right:
        mid = (left + right)//2

        if s[mid] == leftLetter:
            left = mid + 1
            partitionIdx = mid

        else:
            right = mid - 1

    return partitionIdx + 1 , leftLetter

def getCounts(s):
    count, leftLetter = SearchPartitionStart(s)

    return (count, len(s) - count)  if leftLetter == 'a' else (len(s) - count, count)


print(getCounts('aaaaaaaaa'))