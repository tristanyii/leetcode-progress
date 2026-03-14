# Last updated: 3/14/2026, 1:52:04 AM
1import heapq
2class Solution:
3    def findKthLargest(self, nums: List[int], k: int) -> int:
4        heap = []
5
6        for num in nums:
7            heapq.heappush(heap, num)
8            while len(heap) > k:
9                heapq.heappop(heap)
10
11        return heap[0]
12        