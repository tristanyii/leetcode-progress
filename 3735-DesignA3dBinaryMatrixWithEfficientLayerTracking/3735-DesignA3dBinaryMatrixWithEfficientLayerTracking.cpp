// Last updated: 1/12/2026, 3:12:52 PM
class Matrix3D {
public:
    unordered_map<int, int> count_ones;
    map<int, set<int, greater<int>>, greater<int>> freq_to_xs;
    vector<vector<vector<int>>> grid;

    Matrix3D(int n) {
        for(int i = 0; i < n; i++) {
            freq_to_xs[0].insert(i);
        }
        grid.resize(n);
        for(int i = 0; i < n; i++) {
            grid[i].resize(n);
            for(int j = 0; j < n; j++) {
                grid[i][j].resize(n);
            }
        }
    }
    
    void setCell(int x, int y, int z) {
        if(grid[x][y][z] == 0) {
            grid[x][y][z] = 1;
            int old_count = count_ones[x];
            count_ones[x]++;
    
            int new_count = old_count + 1;
            freq_to_xs[old_count].erase(x);
            if(freq_to_xs[old_count].empty()) {
                freq_to_xs.erase(old_count);
            }
            freq_to_xs[new_count].insert(x);
        }
    }
    
    void unsetCell(int x, int y, int z) {
        if(grid[x][y][z] == 1) {
            grid[x][y][z] = 0;
            int old_count = count_ones[x];
            count_ones[x]--;
    
            int new_count = old_count - 1;
            freq_to_xs[old_count].erase(x);
            if(freq_to_xs[old_count].empty()) {
                freq_to_xs.erase(old_count);
            }
            freq_to_xs[new_count].insert(x);
        }
    }
    
    int largestMatrix() {
        return *freq_to_xs.begin()->second.begin();
    }
};

/**
 * Your Matrix3D object will be instantiated and called as such:
 * Matrix3D* obj = new Matrix3D(n);
 * obj->setCell(x,y,z);
 * obj->unsetCell(x,y,z);
 * int param_3 = obj->largestMatrix();
 */