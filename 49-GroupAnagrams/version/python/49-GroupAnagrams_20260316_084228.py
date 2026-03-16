# Last updated: 3/16/2026, 8:42:28 AM
1class Solution:
2    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
3        groups = defaultdict(list)
4
5        for word in strs:
6            key = ''.join(sorted(word))
7            groups[key].append(word)
8        return list(groups.values())
9        