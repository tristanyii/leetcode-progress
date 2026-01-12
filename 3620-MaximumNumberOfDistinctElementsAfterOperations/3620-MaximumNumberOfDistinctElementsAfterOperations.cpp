// Last updated: 1/12/2026, 3:13:08 PM
class Solution {
public:
    int maxDistinctElements(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());
        int n = nums.size();
    
        int last_selection = INT_MIN;
        int ans = 0;
        for(int i = 0; i < n; i++) {
            int min = nums[i] - k;
            int max = nums[i] + k;

            if(min > last_selection) {
                last_selection = min;
                ans++;
            }
            else if(min <= last_selection && max > last_selection) {
                last_selection++;
                ans++;
            }
        }
        return ans;
    }
};