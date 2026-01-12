// Last updated: 1/12/2026, 3:12:44 PM
class Solution {
public:
    int countPartitions(vector<int>& nums, int k) {
        const int MOD = 1e9 + 7;
        
        int n = nums.size();

        multiset<int> window;
        int windowSum = 0;

        vector<int> dp(n + 1, 0);
        dp[0] = 1;

        for(int i = 0, j = 0; i < n; i++) {
            window.insert(nums[i]);
            windowSum = (windowSum + dp[i]) % MOD;

            while(*window.rbegin() - *window.begin() > k) {
                windowSum = (windowSum - dp[j] + MOD) % MOD;
                window.erase(window.find(nums[j]));
                j++;
            }

            dp[i + 1] = windowSum;
        }

        return dp[n];
    }
};

/*
let dp[i] = number of ways to partition nums using nums[0:i)
dp[0] = 1;

you need to find the latest j such that nums[j] < nums[i] - k or nums[j] > nums[i] + k
for(int i = 1; i <= n; i++) {
    int j = magic();
    for(int k = j; k < i; k++) {
        dp[i] += dp[k];
    }
}
*/