# Last updated: 2/5/2026, 10:25:13 PM
1from collections import defaultdict
2class Solution:
3    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
4
5        hashgroup = defaultdict(list)
6
7        for s in strs:
8            key = ''.join(sorted(s))
9            hashgroup[key].append(s) 
10        
11        return list(hashgroup.values())
12        