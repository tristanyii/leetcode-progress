// Last updated: 1/12/2026, 3:13:34 PM
class Solution {
public:
    long long numSubarrays(int num) {
        return (long long) num * (num + 1) / 2;
    }

    long long countAlternatingSubarrays(vector<int>& nums) {
        long long ans = 0;
        int n = nums.size();
        for(int i = 0; i < n;) {
            int j = i + 1;
            bool prevVal = nums[i];
            while(j < n && !prevVal == nums[j]) {
                j++;
                prevVal = !prevVal;
            }
            ans += numSubarrays(j - i);
            i = j;
        }
        return ans;
    }
};