// Last updated: 1/12/2026, 3:12:51 PM
class Solution {
public:
    int maxDifference(string s) {
        vector<int> cnt(26, 0);
        for(char c : s) {
            cnt[c - 'a']++;
        }
        int maxOdd = INT_MIN, minEven = INT_MAX;
        for(int i = 0; i < 26; i++) {
            if(cnt[i] == 0) continue;
            if(cnt[i] & 1) {
                maxOdd = max(maxOdd, cnt[i]);
            } else {
                minEven = min(minEven, cnt[i]);
            }
        }
        return maxOdd - minEven;
    }
};