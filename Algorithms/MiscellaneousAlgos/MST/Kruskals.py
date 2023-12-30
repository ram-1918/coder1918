"""
Kruskal's Algorithm - Greedy algorithm for graphs

It is used to find the MST of a given weighted graph

Idea
1. Sort all edges of the given graph in increasing order
2. Add nodes and edges to the MST in order such that the new edge does not form a cycle
3. By doing so we can say it is making a locally optimal choice (picking smallest weight),
at each step in order to find a glabally optimal solution - Greedy algorithm 

Algorithm
---------
1. Sort edges by weight in increasing order
2. Add each edge to mst if it does not form a cycle, else skip it
3. repeat this until mst has V-1 edges

Detecting cyccle in a graph can be done by Union-Find
"""

class UF:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0]*n
    
    def find(self, node): # path compression
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    
    def union(self, src, dest): # union by rank
        root_src, root_dest = self.find(src), self.find(dest)
        if self.rank[root_src] > self.rank[root_dest]:
            self.parent[root_dest] = self.parent[root_src]
        elif self.rank[root_src] < self.rank[root_dest]:
            self.parent[root_src] = root_dest
        else:
            self.parent[root_dest] = root_src
            self.rank[root_src] += 1

class Graph:
    def __init__(self, vertices):
        self.v = vertices
        self.graph = []
        self.mst = []
    
    def addEdge(self, weight, src, dest):
        self.graph.append([weight, src, dest])
    
    def kruskalsAlgorithm(self):
        uf = UF(self.v) # create an instance for union-find

        # 1. sort edges by weight - Greedy approach to sort edges so that it starts from the minimum weight
        self.graph.sort(key = lambda x: x[0])

        edge_count = curr = 0
        
        # 2. loop over the edges and add perform union operation if an edge doesnt form a cycle
        # Construct MST
        for edge in self.graph: # loop until edge_count is >= v-1 or curr_idx is >= # of vertices
            _, src, dest = edge # self.graph[curr]
            # Break if edge count exceeds (v - 1)
            if edge_count > self.v:
                break
            root_src, root_dest = uf.find(src), uf.find(dest)
            if root_src != root_dest: # it means their root nodes are not same, so this edge doesn't form a cycle
                # we can also calculate total weight here
                edge_count += 1
                self.mst.append(edge)
                uf.union(src, dest)
    
    def findTotalCost(self):
        cost = 0
        for mst_edge in self.mst:
            cost += mst_edge[0]
        return cost




if __name__ == '__main__':
    edges1 = [[10, 0, 1], [6, 0, 2], [5, 0, 3], [15, 1, 3], [4, 2, 3]]
    edges2 = [[4,0,1], [8,1,2], [7,2,3], [9,3,4], [10,4,5], [2,5,6], [6,6,8], [2,8,2], [7,7,8], [1,7,6], [8,0,7], [11,1,7], [14,3,5], [4,2,5]]

    graph = Graph(len(edges2))
    for edge in edges2:
        graph.addEdge(*edge)
    graph.kruskalsAlgorithm()

    cost = graph.findTotalCost()
    
    print(cost)
