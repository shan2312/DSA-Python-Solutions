class Solution:
    def climbStairs(self, n: int) -> int:
        count_ways_with_single_step = 1
        count_ways_with_double_step = 1

        current_step = (n - 2)

        while current_step >= 0:
            count_ways_with_single_step, count_ways_with_double_step = (count_ways_with_single_step + count_ways_with_double_step), count_ways_with_single_step
            current_step -= 1

        return count_ways_with_single_step


if __name__ == '__main__':
    s = Solution()
    print(s.climbStairs(3))
