# Last updated: 1/12/2026, 3:12:40 PM
class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def sumOfDigits(num: int) -> int:
            summ = 0
            while num > 0:
                summ += num%10
                num //= 10
            return summ

        dig_sum = [(num,sumOfDigits(num)) for num in nums]
        sorted_dig_sum = sorted(dig_sum, key = lambda x: (x[1],x[0]))
        
        
        adj_list = {}
        for i in range(len(sorted_dig_sum)):
            head = sorted_dig_sum[i][0]
            tail = dig_sum[i][0]
            if head != tail:
                adj_list[head] = tail

        already_seen = set()
        swaps = 0
        
        for node in adj_list.keys():
            if node in already_seen:
                continue
            cycle_nodes = set()
            cycle_nodes.add(node)
            next_node = adj_list[node]

            while True:
                if next_node in cycle_nodes:
                    break
                cycle_nodes.add(next_node)
                next_node = adj_list[next_node]

            swaps += len(cycle_nodes) - 1
            already_seen.update(cycle_nodes)

        return swaps



        
        