# Last updated: 3/16/2026, 8:41:10 AM
1class Solution:
2    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
3        groups = defaultdict(list)
4
5        for word in strs:
6            count = [0] * 26
7            for letter in word:
8                count[ord(letter) - ord('a')] += 1
9            groups[tuple(count)].append(word)
10        return list(groups.values())
11        