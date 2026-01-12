# Last updated: 1/12/2026, 3:13:04 PM
class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        
        # sort the array
        nums.sort()

        count = 0
        curr = nums[0]-k-1

        for num in nums:

            # set it equal to minimum of the last thing we set + 1
            # and num - k.
            attempt = max(curr + 1, num - k)

            # if that is less than num + k, update count
            if attempt <= num + k:

                count += 1
                curr = attempt

        return count
