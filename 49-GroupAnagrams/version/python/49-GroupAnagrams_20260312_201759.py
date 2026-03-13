# Last updated: 3/12/2026, 8:17:59 PM
1from collections import defaultdict
2class Solution:
3    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
4        hashMap = defaultdict(list)
5
6        for str in strs:
7            key = ''.join(sorted(str))
8
9            hashMap[key].append(str)
10
11        return list(hashMap.values())
12