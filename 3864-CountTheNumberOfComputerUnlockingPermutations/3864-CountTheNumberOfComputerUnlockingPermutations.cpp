// Last updated: 1/12/2026, 3:12:38 PM
class Solution {
public:
    int factorial(int n) {
        const int MOD = 1e9 + 7;
        long long ans = 1;
        for(int i = 1; i <= n; i++) {
            ans = ((ans % MOD) * (i % MOD)) % MOD;
        }

        return (int) ans % MOD;
    }
    
    int countPermutations(vector<int>& complexity) {
        vector<int> copy = complexity;
        sort(copy.begin(), copy.end());
        if(copy[0] != complexity[0] || copy[0] == copy[1]) {
            return 0;
        }

        int n = complexity.size();
        return factorial(n - 1);
    }
};

/*
how many ways are there to order complexity such that 
for every j, there is some index i < j, s.t. complexity[i] < complexity[j]


1 -> 2 -> 3
1 -> 3 -> 2
*/