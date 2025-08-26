# Last updated: 8/26/2025, 12:32:00 AM
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        vals = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        total = 0
        n = len(s)
        for i, ch in enumerate(s):
            # If this numeral is less than the next one, subtract it;
            # otherwise, add it.
            if i + 1 < n and vals[ch] < vals[s[i + 1]]:
                total -= vals[ch]
            else:
                total += vals[ch]
        return total
