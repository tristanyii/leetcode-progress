# Last updated: 1/12/2026, 3:12:36 PM
class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        def sumOfDigits(num):
            summ = 0
            while num > 0:
                summ += num%10
                num //= 10

            return summ

        for i in range(len(nums)):
            if sumOfDigits(nums[i]) == i:
                return i

        return -1