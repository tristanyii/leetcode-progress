// Last updated: 1/12/2026, 3:12:57 PM
struct hash_pair {
    template <class T1, class T2>
    size_t operator()(const pair<T1, T2>& p) const
    {
        // Hash the first element
        size_t hash1 = hash<T1>{}(p.first);
        // Hash the second element
        size_t hash2 = hash<T2>{}(p.second);
        // Combine the two hash values
        return hash1
               ^ (hash2 + 0x9e3779b9 + (hash1 << 6)
                  + (hash1 >> 2));
    }
};

class Solution {
public:
    pair<int, int> simplify(pair<int, int> x) {
        int gcd = __gcd(x.first, x.second);
        return make_pair(x.first / gcd, x.second / gcd);
    }

    long long numberOfSubsequences(vector<int>& nums) {
        int n = nums.size();
        unordered_map<pair<int, int>, vector<int>, hash_pair> st;
        for(int i = 0; i < n; i++) {
            for(int j = i + 2; j < n; j++) {
                pair<int, int> ratio = simplify(make_pair(nums[i], nums[j]));
                st[ratio].push_back(j);
            }
        }

        for(auto &x : st) {
            sort(x.second.begin(), x.second.end());
        }

        long long ret = 0;
        
        for(int r = 4; r < n; r++) {
            for(int s = r + 2; s < n; s++) {
                pair<int, int> ratio = simplify(make_pair(nums[s], nums[r]));
                int idx = upper_bound(st[ratio].begin(), st[ratio].end(), r - 2) - st[ratio].begin();
                ret += idx;
            }
        }
        
        return ret;
    }
};