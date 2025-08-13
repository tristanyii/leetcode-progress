# Last updated: 8/12/2025, 9:16:26 PM
class Solution(object):
    def reverseVowels(self, s):
        s = list(s)
        left = 0
        right = len(s) - 1
        vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        while left < right:
            if s[left] not in vowels:
                left += 1
            elif s[right] not in vowels:
                right -= 1
            
            else: 
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
        
        return "".join(s)

            
            

        