# Last updated: 1/12/2026, 3:13:06 PM
class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        
        # start on an index where the value is 0
        # go left or right
        # if new is also zero, keep going
        # if > 0, subtract 1 from current value and reverse direction

        # valid if we can get rid of all positives

        # return number of valid (curr, direction) combos

        # ideas
            # brute force, loop through zeros and directions and try them
            # find some invariant
                # seems doable. seems like it is just we want to balance on both sides
                # OR one side is one bigger and we have to go that way.

        # this seems like some clever algo

        # start building the sum until we get to 2 past 
        selections = 0

        # get the total sum (one pass)
        leftover = sum(nums)
        current = 0

        for num in nums:
            if num == 0:
                if abs(leftover - current) == 0:
                    selections += 2
                elif abs(leftover - current) == 1:
                    selections += 1

            leftover -= num
            current += num
            if current-leftover > 1:
                break

        return selections



