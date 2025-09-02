# Last updated: 9/1/2025, 9:15:34 PM
class Solution(object):
    def mySqrt(self, x):
        if x == 0:
            return 0

        left, right = 1, x
        ans = 0

        while left <= right:
            mid = left + (right - left) // 2
            square = mid * mid

            if square == x:
                return mid
            elif square < x:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans