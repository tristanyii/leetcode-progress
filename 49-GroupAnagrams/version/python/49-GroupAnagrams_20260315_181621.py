# Last updated: 3/15/2026, 6:16:21 PM
1class Solution:
2    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
3        hash_map = defaultdict(list)
4
5        for word in strs:
6            count = [0] * 26
7
8            for char in word:
9                count[ord(char) - ord('a')] += 1
10
11            key = tuple(count)
12            hash_map[key].append(word)
13
14        return list(hash_map.values())