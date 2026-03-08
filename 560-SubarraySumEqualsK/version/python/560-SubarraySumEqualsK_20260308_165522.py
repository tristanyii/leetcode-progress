# Last updated: 3/8/2026, 4:55:22 PM
1class Solution:
2    def subarraySum(self, nums: List[int], k: int) -> int:
3        count = 0
4        prefix = 0
5        hashmap = {0: 1}   # VERY important
6        
7        for num in nums:
8            prefix += num
9            
10            if prefix - k in hashmap:
11                count += hashmap[prefix - k]
12            
13            hashmap[prefix] = hashmap.get(prefix, 0) + 1
14        
15        return count