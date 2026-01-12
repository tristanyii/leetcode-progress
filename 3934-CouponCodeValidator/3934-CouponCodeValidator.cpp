// Last updated: 1/12/2026, 3:12:31 PM
class Solution {
public:
    vector<string> validateCoupons(vector<string>& code, vector<string>& businessLine, vector<bool>& isActive) {
        vector<int> ordering;

        unordered_map<string, int> businessLines;
        businessLines["electronics"] = 0;
        businessLines["grocery"] = 1;
        businessLines["pharmacy"] = 2;
        businessLines["restaurant"] = 3;
        
        for(int i = 0; i < code.size(); i++) {
            bool ok = true;
            for(int j = 0; j < code[i].size(); j++) {
                if(!isalnum(code[i][j]) && code[i][j] != '_') {
                    ok = false;
                }
            }

            if(code[i].size() == 0) {
                ok = false;
            }

            if(businessLines.find(businessLine[i]) == businessLines.end()) {
                ok = false;
            }

            if(!isActive[i]) {
                ok = false;
            }

            if(ok) {
                ordering.push_back(i);
            }
        }

        sort(ordering.begin(), ordering.end(), 
            [&](const int a, const int b) {
                if(businessLine[a] != businessLine[b]) {
                    return businessLines[businessLine[a]] < businessLines[businessLine[b]];
                }
                return code[a] < code[b];
            });

        vector<string> ans;

        for(int idx : ordering) {
            ans.push_back(code[idx]);
        }
        return ans;
    }
};