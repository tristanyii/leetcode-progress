# Last updated: 9/10/2025, 12:51:41 PM
class Solution(object):
    def isPalindrome(self, x):
        s = str(x)
        l, r = 0, len(s) - 1


        while l < r:
            if s[l] != s[r]:
                return False
            else:
                l += 1
                r -= 1
        return True

        