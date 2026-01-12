// Last updated: 1/12/2026, 3:12:54 PM
class Solution {
    public long calculateScore(String[] instructions, int[] values) {
        boolean[] visited = new boolean[instructions.length];

        int nextIndex = 0;
        
        long score = 0;

        while(nextIndex >= 0 && nextIndex < instructions.length && visited[nextIndex] == false){
            visited[nextIndex] = true;
            if(instructions[nextIndex].equals("add")){
                score += values[nextIndex];
                nextIndex++;
                continue;
            }
            if(instructions[nextIndex].equals("jump")){
                nextIndex = nextIndex + values[nextIndex];
            }
        }

        return score;
    }
}