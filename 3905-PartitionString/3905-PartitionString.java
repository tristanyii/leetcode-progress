// Last updated: 1/12/2026, 3:12:33 PM
class Solution {
    public List<String> partitionString(String s) {
        StringBuilder sb = new StringBuilder();
        HashSet<String> set = new HashSet<>();
        List<String> ret = new ArrayList<>();
        for (int i = 0;i < s.length();i++) {
            sb.append(s.charAt(i));
            if (!set.contains(sb.toString())) {
                set.add(sb.toString());
                ret.add(sb.toString());
                sb = new StringBuilder();
            }
        }
        return ret;
    }
}