# Last updated: 3/15/2026, 6:58:43 PM
1class Solution:
2    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
3        hashmap = defaultdict(list)
4
5        for word in strs:
6            count = [0] * 26
7
8            for char in word:
9                count[ord(char) - ord('a')] += 1
10            key = tuple(count)
11            hashmap[key].append(word)
12
13        return list(hashmap.values())
14        