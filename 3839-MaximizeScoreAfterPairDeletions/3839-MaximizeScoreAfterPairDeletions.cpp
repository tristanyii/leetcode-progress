// Last updated: 1/12/2026, 3:12:42 PM
class Solution {
public:
    int maxScore(vector<int>& nums) {
        int sum = 0;
        for(int num : nums) {
            sum += num;
        }

        int minSum = INT_MAX;
        int minValue = nums[0];
        int n = nums.size();

        if(n <= 2) {
            return 0;
        }

        for(int i = 1; i < n; i++) {
            minSum = min(minSum, nums[i] + nums[i - 1]);
            minValue = min(minValue, nums[i]);
        }

        return sum - (n % 2 == 0 ? minSum : minValue);
    }
};