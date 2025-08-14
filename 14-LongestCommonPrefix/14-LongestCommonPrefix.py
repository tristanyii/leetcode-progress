# Last updated: 8/14/2025, 12:21:27 PM
class Solution(object):
    def longestCommonPrefix(self, strs):
        prefix = strs[0]
        for i in range(len(prefix)):
            for word in strs:
                if i == len(word) or prefix[i] != word[i]:
                    return prefix[:i]
        return prefix
