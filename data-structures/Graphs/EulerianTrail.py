"""
Eulerian Path/Trail/circuit
Definition:
1. An Eulerian Trail is a trail in a graph that visits every edge exactly once. If the trail ends at the starting vertex, it is called an Eulerian Circuit.
2. Eulerian Trails are applicable to graphs where every vertex has an even degree (all vertices are connected with an even number of edges).

Euler's Theorem:
1. A connected graph has an Eulerian Circuit if and only if every vertex has an even degree.
2. A connected graph has an Eulerian Trail if and only if it has exactly two vertices with an odd degree.

Use Cases:
Eulerian Trails are often used in problems involving finding a sequence of edges that covers all edges in a graph exactly once.


Hierholzer's algorithm is used to find Eulerian Trail/Path/circuit

Hierholzer's Algorithm
-----------------------
1. Eulerian trail/path is trail in a finite graph that visits every edge exactly once (allowing for revisiting vertices)
2. Eulierian circuit or cycle is a trail that starts and ends on the same vertex.
3. The basic idea of Hierholzer's algorithm is the step-wise construction of Eulierian cycle by connecting dijunctive circles
4. "To put it other way, before adding the last airport in the final path, we have visited all its outgoing vertex"
5. Postorder DFS - Iterate over all the neighbors first and "remove each edge with the source"
"""
# Reconstucting itinerary
import collections

def constructItinrary(flights):
    # create adj graph
    adj = collections.defaultdict(list)
    for src, dest in flights:
        adj[src].append(dest)
    
    # sort all the destinitions
    for _, destinitions in adj.items():
        destinitions.sort(reverse=True)

    # Traverse over the edges and remove it from the graph
    def dfs(start):
        adj_nodes = adj[start]
        while adj_nodes:
            node = adj_nodes.pop()
            dfs(node)
        trail.append(start)
    
    dfs('JFK') # starting point is fixed

if __name__ == '__main__':
    flights = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
    trail = []
    constructItinrary(flights)
    print(trail[::-1])