// Last updated: 1/12/2026, 3:13:01 PM
class Solution {
public:
    bool checkValidCuts(int d, vector<vector<int>>& rectangles) {
        sort(rectangles.begin(), rectangles.end(), [](const vector<int>& a, const vector<int>& b) {
            if(a[0] == b[0]) {
                return a[2] < b[2];
            }
            return a[0] < b[0];
        });

        int numXIntervals = 0, numYIntervals = 0;
        int n = rectangles.size();
        for(int i = 0; i < n; ) {
            int j = i;
            int mx = rectangles[i][2];
            while(j < n && rectangles[j][0] < mx) {
                mx = max(mx, rectangles[j][2]);
                j++;
            }
            numXIntervals++;
            i = j;
        }

        sort(rectangles.begin(), rectangles.end(), [](const vector<int>& a, const vector<int>& b) {
            if(a[1] == b[1]) {
                return a[3] < b[3];
            }
            return a[1] < b[1];
        });

        for(int i = 0; i < n; ) {
            int j = i;
            int mx = rectangles[i][3];
            while(j < n && rectangles[j][1] < mx) {
                mx = max(mx, rectangles[j][3]);
                j++;
            }
            numYIntervals++;
            i = j;
        }
        return numXIntervals > 2 || numYIntervals > 2;
    }
};