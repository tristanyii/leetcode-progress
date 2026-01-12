# Last updated: 1/12/2026, 3:12:55 PM
from collections import defaultdict
from typing import List

class Solution:
    def baseUnitConversions(self, conversions: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        weights = {}

        # Build directed graph
        for u, v, w in conversions:
            graph[u].append(v)
            weights[(u, v)] = w

        # Number of nodes
        n = max(max(u, v) for u, v, _ in conversions) + 1
        ret = [0] * n
        ret[0] = 1  # base multiplier is always 1

        def dfs(node):
            for nei in graph[node]:
                if ret[nei] == 0:   # only visit unassigned nodes
                    ret[nei] = (ret[node] * weights[(node, nei)]) % (10**9 + 7)
                    dfs(nei)

        dfs(0)
        return ret
