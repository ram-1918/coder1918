"""
Prim's Algorithm - greedy algorithms on graphs
-----------------
It is a greedy algorithm used to find the minimum spanning tree problem.
It always starts with a single node and moves through serveral adjacent edges, inorder to explore all connected components along the way.
"""

class Prims:
    def __init__(self, vertices):
        self.v = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]
        self.distance = [float('inf')] * self.v # 
        self.parent = [None] * self.v # 
        self.mstset = [False] * self.v # included or not in Shortest path tree. False - not included in shortest path tree and True - Vice versa
        self.distance[0] = 0
        self.parent[0] = -1
    
    # Find the minimum key which is not yet included in MST
    def findMinKey(self):
        min_key = float('inf')
        for v in range(self.v): # traverse over all the keys until min_index is found
            if self.distance[v] < min_key and self.mstset[v] == False:
                min_key = self.distance[v]
                min_index = v
        return min_index
    
    def prims(self):
        for _ in range(self.v):
            min_indexed_src = self.findMinKey() # greedily selects the node with minimum key
            self.mstset[min_indexed_src] = True
            for dest_v in range(self.v):
                curr_node = self.graph[min_indexed_src][dest_v]
                # curr_node value > 0 and curr_node is not in MST and weight of [dest] > weight on the graph 
                if curr_node > 0 and self.mstset[dest_v] == False and self.distance[dest_v] > curr_node:
                    self.distance[dest_v] = curr_node
                    self.parent[dest_v] = min_indexed_src
        
        self.displayTree()
        print(self.parent)
        print(self.distance)
        print(self.mstset)
    
    def displayTree(self):
        for i in range(1, self.v):
            print(f'{self.parent[i]} - {i}: {self.graph[i][self.parent[i]]}\n')
    

if __name__ == '__main__':
    vertices = 5
    graph = Prims(vertices)
    graph.graph = [[0, 2, 0, 6, 0],
                   [2, 0, 3, 8, 5],
                   [0, 3, 0, 0, 7],
                   [6, 8, 0, 0, 9],
                   [0, 5, 7, 9, 0]]
    graph.prims()