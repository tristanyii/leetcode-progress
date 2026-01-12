// Last updated: 1/12/2026, 3:12:35 PM
class Solution {
public:
    int calculateMoves(vector<int> nums, int badNum) {
        int moves = 0;
        int n = nums.size();
        for(int i = 0; i < nums.size() - 1; i++) {
            if(nums[i] == badNum) {
                nums[i] *= -1;
                nums[i + 1] *= -1;
                moves++;
            }
        }

        if(nums[n - 1] == badNum) {
            return INT_MAX;
        }
        return moves;
    }
    
    bool canMakeEqual(vector<int>& nums, int k) {
        int n = nums.size();

        int ans = min(calculateMoves(nums, 1), calculateMoves(nums, -1));
        return ans <= k;
    }
};