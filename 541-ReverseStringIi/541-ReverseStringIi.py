# Last updated: 8/12/2025, 9:16:25 PM
class Solution(object):
    def reverseStr(self, s, k):
        s = list(s)
        i = 0
        while i < len(s):
            j = min(i + k - 1, len(s) - 1)
            left, right = i, j
            while left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
            i += 2 * k
        return "".join(s)
