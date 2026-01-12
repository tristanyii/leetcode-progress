# Last updated: 1/12/2026, 3:13:35 PM
class Solution(object):
    def isSubstringPresent(self, s):
        """
        :type s: str
        :rtype: bool
        """
        seenlens = set()
        for i in range(1, len(s)):
            curr = s[i-1:i+1]
            seenlens.add(curr)
            if curr[::-1] in seenlens:
                return True
        return False
            
        