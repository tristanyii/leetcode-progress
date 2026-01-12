# Last updated: 1/12/2026, 3:13:37 PM
class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        k=0
        for i in nums:
            i=str(i)
            k+=int(max(i)*len(i))
        return k
    
    #finding the highest digit may be a challenge