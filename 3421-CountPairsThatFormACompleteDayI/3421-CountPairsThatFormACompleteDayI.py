# Last updated: 1/12/2026, 3:13:28 PM
from collections import defaultdict
class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        # 4:22

        # 0:23
        for i in range(len(hours)):
            hours[i] = hours[i] % 24

        print(hours)
        comps = defaultdict(int)

        # [3,0,2,3,9,4]
        ans = 0
        for hour in hours:
            comp = (24-hour) % 24
            if comp in comps:
                ans += comps[comp]
            
            comps[hour] += 1

        return ans