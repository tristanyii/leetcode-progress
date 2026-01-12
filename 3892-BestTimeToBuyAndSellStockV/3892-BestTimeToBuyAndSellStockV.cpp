// Last updated: 1/12/2026, 3:12:33 PM
class Solution {
public:
    vector<int> _prices;
    int _k;
    vector<vector<vector<vector<long long>>>> dp;

    long long recurse(int i, bool isLongPosition, bool isTransactionOngoing, int numTransactions) {
        if(numTransactions >= _k) {
            return 0;
        }

        if(i == _prices.size()) {
            if(isTransactionOngoing) {
                return -1e15;
            }
            return 0;
        }

        if(dp[i][isLongPosition][isTransactionOngoing][numTransactions] != -1) {
            return dp[i][isLongPosition][isTransactionOngoing][numTransactions];
        }

        long long maxProfit = recurse(i + 1, isLongPosition, isTransactionOngoing, numTransactions);
        if(isTransactionOngoing) {
            if(isLongPosition) {
                maxProfit = max(maxProfit, _prices[i] + recurse(i + 1, true, false, numTransactions + 1));
            } else {
                maxProfit = max(maxProfit, -(_prices[i]) + recurse(i + 1, false, false, numTransactions + 1));
            }
        } else {
            maxProfit = max(maxProfit, -(_prices[i]) + recurse(i + 1, true, true, numTransactions));
            maxProfit = max(maxProfit, _prices[i] + recurse(i + 1, false, true, numTransactions));
        }

        return (dp[i][isLongPosition][isTransactionOngoing][numTransactions] = maxProfit);
    }

    long long maximumProfit(vector<int>& prices, int k) {
        _prices = prices;
        _k = k;

        int n = prices.size();

        dp.assign(n,
            vector<vector<vector<long long>>>(2,
            vector<vector<long long>>(2,
            vector<long long>(k, -1))));

        return recurse(0, false, false, 0);
    }
};