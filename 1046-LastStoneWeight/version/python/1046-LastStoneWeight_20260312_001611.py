# Last updated: 3/12/2026, 12:16:11 AM
1import heapq
2class Solution:
3    def lastStoneWeight(self, stones: List[int]) -> int:
4
5        maxheap = [-stone for stone in stones]
6        heapq.heapify(maxheap)
7
8        while len(maxheap) > 1:
9            y = -heapq.heappop(maxheap)
10            x = -heapq.heappop(maxheap)
11
12            if x != y:
13                heapq.heappush(maxheap, -(y - x))
14
15        return -maxheap[0] if maxheap else 0
16
17
18        