# Last updated: 1/12/2026, 3:12:49 PM
class Solution:
    def hasSameDigits(self, s: str) -> bool:
        
        # convert s to an array of integer digits
        s = [int(d) for d in str(s)]

        while len(s) > 2:

            #compute the new digits for everything in s
            new_list = []
            for i in range(len(s)-1):
                new_list.append((s[i] + s[i+1]) % 10)

            s = new_list

        return s[0] == s[1]
