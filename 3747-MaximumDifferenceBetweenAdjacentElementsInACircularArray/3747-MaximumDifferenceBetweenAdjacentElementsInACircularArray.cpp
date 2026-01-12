// Last updated: 1/12/2026, 3:12:50 PM
class Solution {
public:
    int maxAdjacentDistance(vector<int>& nums) {
        int mx = 0;
        for(int i = 0; i < nums.size() - 1; i++) {
            mx = max(mx, abs(nums[i + 1] - nums[i]));
        }
        return max(mx, abs(nums[nums.size() - 1] - nums[0]));
    }
};