# Last updated: 1/12/2026, 3:13:31 PM
class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
        vowCount = 0
        digits = 0
        vowels = set(['a','e','i','o','u'])
        for c in word:
            if c.isdigit():
                digits +=1
            elif c.isalpha():
                if c.lower() in vowels:
                    vowCount+=1
            else:
                return False
        if vowCount == 0:
            return False
        return len(word) - vowCount-digits >= 1