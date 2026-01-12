// Last updated: 1/12/2026, 3:13:37 PM
class DSU {
public:
    DSU(int n) {
        for(int i = 0; i < n; i++) {
            parent.push_back(i);
            ands.push_back(INT_MAX);
        }
    }

    int get(int a) {
        if(a == parent[a]) return a;
        return parent[a] = get(parent[a]);
    }

    int getAnd(int a) {
        return ands[get(a)];
    }

    void merge(int a, int b, int w) {
        int p1 = get(a), p2 = get(b);
        
        int val = ands[p1] & ands[p2] & w;
        ands[p1] = val;
        ands[p2] = val;
        parent[p2] = p1;
    }

private:
    vector<int> parent;
    vector<int> ands;
};

class Solution {
public:
    vector<int> minimumCost(int n, vector<vector<int>>& edges, vector<vector<int>>& query) {
        vector<int> ans;
        DSU dsu(n);
        
        for(int i = 0; i < edges.size(); i++) {
            dsu.merge(edges[i][0], edges[i][1], edges[i][2]);
        }

        for(int i = 0; i < query.size(); i++) {
            int a = query[i][0], b = query[i][1];
            if(dsu.get(a) != dsu.get(b)) {
                ans.push_back(-1);
            } else {
                ans.push_back(dsu.getAnd(a));
            }
        }
        
        return ans;
    }
};