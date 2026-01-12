# Last updated: 1/12/2026, 3:12:58 PM
class Solution:
    def countGoodArrays(self, n, m, k):
        MOD = 10**9 + 7

        # Precompute factorials and inverse factorials
        fact = [1] * (n)
        inv_fact = [1] * (n)

        for i in range(1, n):
            fact[i] = fact[i - 1] * i % MOD

        inv_fact[n - 1] = pow(fact[n - 1], MOD - 2, MOD)
        for i in range(n - 2, -1, -1):
            inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD

        def comb(a, b):
            if b < 0 or b > a:
                return 0
            return fact[a] * inv_fact[b] % MOD * inv_fact[a - b] % MOD

        result = comb(n - 1, k) * m % MOD
        result = result * pow(m - 1, n - 1 - k, MOD) % MOD
        return result
