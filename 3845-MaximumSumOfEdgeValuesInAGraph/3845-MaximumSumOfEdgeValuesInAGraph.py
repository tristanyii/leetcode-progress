# Last updated: 1/12/2026, 3:12:41 PM
class Solution:
    def maxScore(self, n: int, edges: List[List[int]]) -> int:

        def recurse(n: int) -> int:
            if n == 1: return 0
            if n == 2: return 2
            if n == 3: return 3
            return (n * (n-2)) + recurse(n-2)

        #Grabs the max sum possible given that graph is a ring
        def getSum(n: int) -> int:
            return (n * (n-1)) + (n * (n-2)) + recurse(n - 1) + recurse(n - 2)

        if len(edges) == 1: return 2
        
        node_counter = defaultdict(int)

        #calculate how many nodes each node is connected to
        for edge in edges:
            a = edge[0]
            b = edge[1]
            node_counter[a] += 1
            node_counter[b] += 1

        #check if graph is a ring or line
        for node in node_counter.keys():
            if node_counter[node] == 1:
                return getSum(n) - 2
            
        return getSum(n)