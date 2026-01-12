# Last updated: 1/12/2026, 3:13:24 PM
class Solution:
    def minimumLength(self, s: str) -> int:

        from collections import Counter

        #keep a dictionary that matches the alphabet to its occurence

        dicti = Counter(s)

        while max(dicti.values())>=3:
            max_key = max(dicti, key=dicti.get)
            if dicti[max_key] >=3: 
                dicti[max_key]-=2
            
        res=0
        for count in dicti.values():
            res+=count
        return res

        
        #result: min length of the final string you can achieve

