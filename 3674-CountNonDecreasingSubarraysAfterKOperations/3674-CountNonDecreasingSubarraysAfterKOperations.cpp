// Last updated: 1/12/2026, 3:13:00 PM
class Solution {
public:
    long long countNonDecreasingSubarrays(vector<int>& nums, int k) {
        reverse(nums.begin(), nums.end());
        
        int n = nums.size();
        deque<int> dq;
        long long curOperations = 0;
        long long ret = 0;
        int j = 0;
        for(int i = 0; i < n; i++) {
            while(!dq.empty() && nums[i] > nums[dq.back()]) {
                int rightIndex = dq.back();
                dq.pop_back();
                int leftIndex = dq.empty() ? (j - 1) : dq.back();

                curOperations += 1LL * (rightIndex - leftIndex) * (nums[i] - nums[rightIndex]);
            }
            
            dq.push_back(i);
            
            while(curOperations > k) {
                int cur = dq.front();
                curOperations += (nums[j] - nums[cur]);
                if(dq.front() == j) {
                    dq.pop_front();
                }
                j++;
            }
            ret += (i - j + 1);
        }
        return ret;
    }
};