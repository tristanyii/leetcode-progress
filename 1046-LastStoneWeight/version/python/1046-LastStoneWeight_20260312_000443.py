# Last updated: 3/12/2026, 12:04:43 AM
1import heapq
2class Solution:
3    def lastStoneWeight(self, stones: List[int]) -> int:
4        maxheap = [-stone for stone in stones]
5        heapq.heapify(maxheap)
6
7        while len(maxheap) > 1:
8            y = -heapq.heappop(maxheap)
9            x = -heapq.heappop(maxheap)
10
11            if y != x:
12                heapq.heappush(maxheap, -(y - x))
13
14        
15        return -maxheap[0] if maxheap else 0
16        