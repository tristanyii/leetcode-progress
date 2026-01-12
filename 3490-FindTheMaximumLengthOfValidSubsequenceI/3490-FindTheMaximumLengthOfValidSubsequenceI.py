# Last updated: 1/12/2026, 3:13:17 PM
class Solution(object):
    def maximumLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        evenStreak, oddStreak, alternatingStreak = 0, 0, 1
        is_odd = False
        if nums[0] % 2 == 0:
            evenStreak += 1
        else:
            oddStreak += 1
            is_odd = True
        
        for i in range(1, len(nums)):
            if nums[i] % 2 == 0:
                evenStreak += 1
            if nums[i] % 2 == 1:
                oddStreak += 1
            if is_odd and nums[i] % 2 == 0:
                alternatingStreak += 1
                is_odd = False
            if not is_odd and nums[i] % 2 == 1:
                alternatingStreak += 1
                is_odd = True
        return max(evenStreak, oddStreak, alternatingStreak)

        
            




