// Last updated: 1/12/2026, 3:13:17 PM
class Solution {
public:
    int getLargestOutlier(vector<int>& nums) {
        int totalSum = 0;
        unordered_map<int, int> mp;
        for(int x : nums) {
            mp[x]++;
            totalSum += x;
        }
        int mx = INT_MIN;
        for(int x : nums) {
            int target = totalSum - x;
            if(target % 2 == 0 && (mp[target / 2] - ((target / 2 == x) ? 1 : 0) >= 1)) {
                mx = max(mx, x);
            }
        }
        return mx;
    }
};