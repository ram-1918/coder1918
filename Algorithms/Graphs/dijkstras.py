"""
Dijkstra's Algorithm
--------------------
It is used to find the shortest paths from source to other vertices
"""

class Dijkstras:
    def __init__(self, vertices):
        self.v = vertices
        self.graph = [[0 for _ in range(self.v)] for _ in range(self.v)]
        self.distance = [float('inf')]*self.v
        self.visited = [False]*self.v
        self.distance[0] = 0 # distance from source to source is 0
    
    def findMinDistance(self):
        min_dis = float('inf')
        for v in range(self.v):
            if self.distance[v] < min_dis and self.visited[v] == False:
                min_dis = self.distance[v]
                min_index = v
        return min_index

    def shortestPath(self):
        for _ in range(self.v):
            min_index = self.findMinDistance()
            self.visited[min_index] = True
            for dest_v in range(self.v):
                curr_node = self.graph[min_index][dest_v]
                if curr_node > 0 and self.visited[dest_v] == False and self.distance[dest_v] > self.distance[min_index] + curr_node:
                    self.distance[dest_v] = self.distance[min_index] + curr_node
        self.printPath()
    
    def printPath(self):
        print(self.distance)

d = Dijkstras(9)
d.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
            [4, 0, 8, 0, 0, 0, 0, 11, 0],
            [0, 8, 0, 7, 0, 4, 0, 0, 2],
            [0, 0, 7, 0, 9, 14, 0, 0, 0],
            [0, 0, 0, 9, 0, 10, 0, 0, 0],
            [0, 0, 4, 14, 10, 0, 2, 0, 0],
            [0, 0, 0, 0, 0, 2, 0, 1, 6],
            [8, 11, 0, 0, 0, 0, 1, 0, 7],
            [0, 0, 2, 0, 0, 0, 6, 7, 0]
            ]

d.shortestPath()