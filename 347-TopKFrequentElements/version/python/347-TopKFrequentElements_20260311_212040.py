# Last updated: 3/11/2026, 9:20:40 PM
1class Solution:
2    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
3        count = Counter(nums)
4        
5        heap = []
6        for num in count:
7            freq = count[num]
8            heapq.heappush(heap, (freq, num))
9
10            if len(heap) > k:
11                heapq.heappop(heap)
12
13        result = []
14
15        for freq, num in heap:
16            result.append(num)
17        return result       