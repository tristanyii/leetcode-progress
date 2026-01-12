// Last updated: 1/12/2026, 3:12:30 PM
class Solution {
public:
    vector<vector<int>> adj;

    void dfs(int i, vector<bool>& visited) {
        if(visited[i]) {
            return;
        }
        visited[i] = true;
        for(int x : adj[i]) {
            dfs(x, visited);
        }
    }
    
    bool check(int t, int n, const vector<vector<int>>& edges, int k) {
        adj.resize(n);
        for(const vector<int>& x : edges) {
            int time = x[2];
            if(time <= t) {
                continue;
            }
            adj[x[0]].push_back(x[1]);
            adj[x[1]].push_back(x[0]);
        }

        int numComponents = 0;
        vector<bool> visited(n, false);
        for(int i = 0; i < n; i++) {
            if(!visited[i]) {
                dfs(i, visited);
                numComponents++;
            }
        }

        adj.clear();

        return numComponents >= k;
    }
    
    int minTime(int n, vector<vector<int>>& edges, int k) {
        int l = 0, r = 1e9 + 5;
        while(l < r) {
            int mid = l + (r - l) / 2;
            if(check(mid, n, edges, k)) {
                r = mid;
            } else {
                l = mid + 1;
            }
        }

        return l;
    }
};