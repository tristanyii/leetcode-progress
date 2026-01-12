// Last updated: 1/12/2026, 3:13:07 PM
class Solution {
    public int possibleStringCount(String word) {
        int n = word.length();
        int ans = 1;
        for(int i = 0; i < n;) {
            int j = i;
            while(j < n && word.charAt(i) == word.charAt(j)) {
                j++;
            }

            ans += (j - i - 1);
            i = j;
        }

        return ans;
    }
}