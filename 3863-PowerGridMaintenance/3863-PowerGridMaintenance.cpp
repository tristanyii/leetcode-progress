// Last updated: 1/12/2026, 3:12:39 PM
class DSU {
public:
    vector<int> parent;
    vector<set<int>> grid;
    vector<int> size;

    DSU(int n) {
        parent.resize(n);
        grid.resize(n);
        size.resize(n);
        for(int i = 0; i < n; i++) {
            parent[i] = i;
            grid[i].insert(i);
            size[i] = 1;
        }
    }

    int getParent(int a) {
        if(parent[a] == a) {
            return a;
        }
        return (parent[a] = getParent(parent[a]));
    }

    void removeFromSet(int a) {
        int parentA = getParent(a);
        grid[parentA].erase(a);
    }

    int getSmallest(int a) {
        int parentA = getParent(a);
        if(grid[parentA].empty()) {
            return -1;
        }
        return *grid[parentA].begin();
    }
    
    void merge(int a, int b) {
        int parentA = getParent(a);
        int parentB = getParent(b);

        if (parentA == parentB) {
            return;
        }


        if(size[parentA] < size[parentB]) {
            parent[parentA] = parentB;
            size[parentB] += grid[parentA].size();
            for(int x : grid[parentA]) {
                grid[parentB].insert(x);
            }
            grid[parentA].clear();
        } else {
            parent[parentB] = parentA;
            size[parentA] += grid[parentB].size();
            for(int x : grid[parentB]) {
                grid[parentA].insert(x);
            }
            grid[parentB].clear();
        }
    }
};

class Solution {
public:
    vector<int> processQueries(int c, vector<vector<int>>& connections, vector<vector<int>>& queries) {
        DSU dsu = DSU(c + 1);
        vector<bool> isOnline(c + 1, true);

        for(vector<int>& x : connections) {
            int u = x[0], v = x[1];
            u, v;
            dsu.merge(u, v);
        }

        vector<int> ans;
        for(vector<int>& x : queries) {
            if(x[0] == 1) {
                if(isOnline[x[1]]) {
                    ans.push_back(x[1]);
                } else {
                    ans.push_back(dsu.getSmallest(x[1]));
                }
            } else {
                dsu.removeFromSet(x[1]);
                isOnline[x[1]] = false;
            }
        }

        return ans;
    }
};