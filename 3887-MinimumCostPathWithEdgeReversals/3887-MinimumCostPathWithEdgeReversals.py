# Last updated: 1/12/2026, 3:12:32 PM
from collections import defaultdict
import heapq
class Solution(object):
    def minCost(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """

        # Dijkstra's algorithm with a twist

        # just take the shortest path out of the curredge and the reverse edge

        table = defaultdict(list)

        for u, v, w in edges:
            table[u].append((v,w))
            table[v].append((u, 2*w))
        

        # initialize a priority queue (minheap)

        minheap = [(0,0)] # initialize w distance, src node

        # keep track of min distances for each node

        dist = {0:0} # node : distance

        while minheap:

            currdist, node = heappop(minheap) # pop node with least weight  
            # if this 
            if currdist > dist.get(node, float('inf')):
                continue

            if node == n - 1:
                return currdist
            
            for neighbor, ecost in table[node]:
                newdist = currdist + ecost

                if newdist < dist.get(neighbor, float('inf')):
                    dist[neighbor] = newdist
                    heappush(minheap, (newdist, neighbor))
        return -1


