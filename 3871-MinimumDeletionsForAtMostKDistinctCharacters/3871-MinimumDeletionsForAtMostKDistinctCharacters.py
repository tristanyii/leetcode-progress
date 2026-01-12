# Last updated: 1/12/2026, 3:12:37 PM
class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        counter = {}
        for c in s:
            if c not in counter:
                counter[c] = 0
            counter[c] += 1
        
        if len(counter.keys()) <= k:
            return 0
        
        queue = sorted(list(counter.values()))
        print(queue)
        
        num_deletions = 0
        for i in range(0,len(counter.keys()) - k):
            num_deletions += queue.pop(0)
        
        return num_deletions