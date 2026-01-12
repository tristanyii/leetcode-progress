# Last updated: 1/12/2026, 3:13:20 PM
class Solution:
    def betterCompression(self, compressed: str) -> str:

        dicti = {}
        i=0
        while i < len(compressed):
            if compressed[i] in "abcdedfghijklmnopqrstuvwxyz":
                number = ""
                alphabet = compressed[i]
                i+=1
                while i<len(compressed) and compressed[i].isdigit():
                    number +=compressed[i]
                    i+=1
                if alphabet in dicti:
                    dicti[alphabet]+=int(number)
                else:
                    dicti[alphabet]=int(number)
                
        res = ""
        for alphabet in sorted(dicti.keys()):
            res+=alphabet
            res+=str(dicti[alphabet])
        return res
        