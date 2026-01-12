# Last updated: 1/12/2026, 3:13:09 PM
class Solution:
    def possibleStringCount(self, word: str) -> int:
        prev = ''
        ret = 1
        for c in word:
            if prev == c:
                ret += 1
                prev = c
            if prev != c:
                prev = c
        return ret