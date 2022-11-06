class NearestSmallerElement:
    def __init__(self) -> None:
        pass

    def get_nearest_element(self, nums):
        stack = []
        result = []

        for num in nums:

            while stack and stack[-1] >= num:
                stack.pop()

            if stack:
                result.append(stack[-1])

            else:
                result.append(-1)
            
            stack.append(num)

        return result

if __name__ == '__main__':
    nse = NearestSmallerElement()
    print(nse.get_nearest_element([1, 3, 0, 2, 5]))