// Last updated: 1/12/2026, 3:13:38 PM
class Solution {
    public int minOperations(int[] nums, int k) {
        PriorityQueue<Integer> pq = new PriorityQueue<>();
    for (int i = 0;i < nums.length;i++) {
            if (nums[i] < k) {
            pq.add(nums[i]);
            }
        
    }
    int count = 0;
    if (pq.size() == 0) {
        return count;
    }
    
    while (pq.size() > 1) {
        int x = pq.poll();
        int y = pq.poll();
        long sum = (long)x*2 + (long)y;
        if (sum < (long)k) {
            pq.add((int)sum);
        }
        count++;
    }
    if (pq.size() == 1) {
        return count+1;
    }
    return count;
    }
}