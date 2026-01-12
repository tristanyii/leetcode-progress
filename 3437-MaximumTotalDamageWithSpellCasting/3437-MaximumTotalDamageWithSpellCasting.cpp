// Last updated: 1/12/2026, 3:13:30 PM
class Solution {
public:
    long long maximumTotalDamage(vector<int>& power) {
        map<int, int> cnt;
        for(int p : power) {
            cnt[p]++;
        }

        map<int, int64_t> dp;
        dp[0] = 0;
        dp[1] = cnt[1];

        for(auto [p, pCnt] : cnt) {
            if(p == 1) continue;
            int64_t maxDamage = 0;

            auto dontTakeIt = dp.lower_bound(p);
            if(dontTakeIt != dp.begin()) {
                dontTakeIt = prev(dontTakeIt);
                maxDamage = max(maxDamage, dontTakeIt->second);
            }

            auto takeIt = dp.lower_bound(p - 2);
            int64_t takeItDamage = 1LL * pCnt * p;
            if(takeIt != dp.begin()) {
                takeIt = prev(takeIt);
                takeItDamage += takeIt->second;
            }
            maxDamage = max(maxDamage, takeItDamage);

            dp[p] = maxDamage;

            cout << maxDamage << "\n";
        }

        return prev(dp.end())->second;
    }
};