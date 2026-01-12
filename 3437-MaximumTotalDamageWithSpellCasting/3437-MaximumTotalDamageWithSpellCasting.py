# Last updated: 1/12/2026, 3:13:28 PM
class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        ct = Counter(power)
        ct = sorted(ct.items())
        dp = [0 for i in range(len(ct))]
        dp[0] = ct[0][0]*ct[0][1]
        for i in range(1,len(ct)):
            cur = dp[i-1]
            alt = ct[i][0]*ct[i][1]
            j = i-1
            while j>=0 and ct[j][0]+2>=ct[i][0]:
                j-=1
            if j>=0:
                alt = dp[j]+ct[i][0]*ct[i][1]
            dp[i] = max(cur, alt)
        print(ct)
        return dp[-1]