// Last updated: 1/12/2026, 3:12:34 PM
class Solution {
    public int countTrapezoids(int[][] points) {
        HashMap<Integer,Integer> yAxis = new HashMap<>();
        long res = 0;
        for (int i = 0;i < points.length;i++) {
          
            int y = points[i][1];
            yAxis.put(y,yAxis.getOrDefault(y,0)+1);
        }
        ArrayList<Long> amounts = new ArrayList<>();
        long prev = 0;
        for (Integer i : yAxis.values()) {
            if (i >= 2) {
               long curr = ((long) i * (i - 1)) / 2;
                res += curr * prev;
                prev += curr;
                

            }
        }
        return (int)(res % (int)(Math.pow(10,9)+7));
    }
}