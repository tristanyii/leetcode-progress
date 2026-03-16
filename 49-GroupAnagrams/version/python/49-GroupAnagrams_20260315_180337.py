# Last updated: 3/15/2026, 6:03:37 PM
1class Solution:
2    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
3        hash_map = defaultdict(list)
4
5        for string in strs:
6            key = ''.join((sorted(string)))
7            hash_map[key].append(string)
8        return list(hash_map.values())