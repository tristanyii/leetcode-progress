// Last updated: 1/12/2026, 3:13:39 PM
class Solution {
    public int minimumOperationsToWriteY(int[][] grid) {
        int n = grid.length;

        int[] yFreq = new int[3];
        int[] nonYFreq = new int[3];

        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                if(isInY(i, j, n)) {
                    yFreq[grid[i][j]]++;
                } else {
                    nonYFreq[grid[i][j]]++;
                }
            }
        }

        int totalY = 0, totalNonY = 0;
        for(int x : yFreq) totalY += x;
        for(int x : nonYFreq) totalNonY += x;

        int ans = Integer.MAX_VALUE;

        for(int yd = 0; yd < 3; yd++){
            for(int bd = 0; bd < 3; bd++){
                if(yd == bd) continue; 

                int yCost = totalY - yFreq[yd];
                int bCost = totalNonY - nonYFreq[bd];

                ans = Math.min(ans, yCost + bCost);
            }
        }

        return ans;
    }

    private boolean isInY(int i, int j, int n) {
        int half = n / 2;

        if (i < half && (j == i || j == n - 1 - i)) return true;

        if (i >= half && j == half) return true;

        return false;
    }
}
