# Last updated: 2/7/2026, 10:49:55 PM
1from collections import defaultdict
2class Solution:
3    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
4
5        hashgroup = defaultdict(list)
6
7        for s in strs:
8            key = ''.join(sorted(s))
9
10            hashgroup[key].append(s)
11
12
13        return list(hashgroup.values())
14