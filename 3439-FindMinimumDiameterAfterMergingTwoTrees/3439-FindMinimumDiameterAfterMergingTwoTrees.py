# Last updated: 1/12/2026, 3:13:26 PM
class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:

        #how do i find a diameter of the new graph? (two trees connected)
        #get the diameter from each node from trees

        #very similar to the diameter of binary tree easy problem

        #first find the longest diameter of each tree
        #then connect the center point of each diameter (and add 1 since we are connecting the trees)

        #result is going to be either D1, D2, or (D1/2 + D2/2)

        #the number of edges will be 1 less thna the number of nodes

        n = len(edges1)+1
        m = len(edges2)+1

        def build_adj(edges):
            adj = defaultdict(list)
            for n1, n2 in edges:
                adj[n1].append(n2)
                adj[n2].append(n1)
            return adj
        
        adj1 = build_adj(edges1)
        adj2 = build_adj(edges2)

        #DFS
        #return two values [diameter, max_leaf_path]

        def get_diameter(cur, par, adj): #this problem itself is a leet medium
            #traverse the graph
            
            max_d = 0
            max_child_paths = [0, 0]

            for nei in adj[cur]:
                if nei == par: #make sure you're not looking at repeated values
                    continue 
                nei_d, nei_max_leaf_path = get_diameter(nei, cur, adj)
                max_d = max(max_d, nei_d)

                heapq.heappush(max_child_paths, nei_max_leaf_path)
                heapq.heappop(max_child_paths) #pop the smallest one so that only the two max paths are left
            
            max_d = max(max_d, sum(max_child_paths))
            return [max_d, 1+max(max_child_paths)]

        d1, _ = get_diameter(0, -1, adj1)
        d2, _ = get_diameter(0, -1, adj2)

        return max(d1, d2, 1+ ceil(d1/2)+ceil(d2/2))
