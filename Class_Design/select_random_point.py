import random

class Solution:
    def __init__(self, rects):
        self.rects = rects
        
        count_of_points = []
        points_count = 0
        for rect in rects:
            a, b, x, y = rect
            points_count += (abs(a - x) + 1)*(abs(b - y) + 1)
            count_of_points.append(points_count)

        self.cum_percentage = [c/count_of_points[-1] for c in count_of_points]

    def get_rectangle_index(self, p_rand):
        left, right = 0, len(self.cum_percentage) - 1

        while left <= right:
            mid = (left + right)//2
            mid_value = self.cum_percentage[mid]

            if p_rand < mid_value:
                right = mid - 1

            elif p_rand > mid_value:
                left = mid + 1

            else:
                return mid
            
        return left

    def pick(self):
        p_rand = random.random()

        rect_index = self.get_rectangle_index(p_rand)

        a, b, x, y = self.rects[rect_index]

        rand_row, rand_col = random.randint(a, x), random.randint(b, y)

        return [rand_row, rand_col]



# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()

s = Solution([[-2, -2, 1, 1], [2, 2, 4, 6]])

print(s.pick())
print(s.pick())
print(s.pick())
print(s.pick())
print(s.pick())
