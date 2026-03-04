# Last updated: 3/4/2026, 5:25:35 PM
1class Solution:
2    def findKthLargest(self, nums: List[int], k: int) -> int:
3        nums.sort()
4
5        return nums[-k]
6        