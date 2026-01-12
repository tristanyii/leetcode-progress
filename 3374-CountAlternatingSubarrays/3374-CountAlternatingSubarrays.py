# Last updated: 1/12/2026, 3:13:36 PM
class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        count = 1
        start = 0
        for end in range(1, len(nums)):
            if nums[end] == nums[end-1]:
                start = end
            count+= end-start+1
        return count
