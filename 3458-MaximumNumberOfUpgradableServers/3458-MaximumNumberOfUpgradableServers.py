# Last updated: 1/12/2026, 3:13:23 PM
class Solution:
    def maxUpgrades(self, count, upgrade, sell, money):
        def valid(c, u, s, m, x):
            return x * u <= m + (c - x) * s

        ret = []

        for i in range(len(count)):
            l, r = 0, count[i]

            while l < r:
                mid = (l + r + 1) // 2  # bias right
                if valid(count[i], upgrade[i], sell[i], money[i], mid):
                    l = mid
                else:
                    r = mid - 1

            ret.append(l)

        return ret
