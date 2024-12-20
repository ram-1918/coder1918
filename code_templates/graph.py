# DFS recurssive
def fn(graph):
    def dfs(node):
        ans = 0
        # do some logic
        for neighbor in graph[node]:
            if neighbor not in seen:
                seen.add(neighbor)
                ans += dfs(neighbor)
        
        return ans

    seen = {'START_NODE'}
    return dfs('START_NODE')

# DFS iterative

def fn(graph):
    stack = ['START_NODE']
    seen = {'START_NODE'}
    ans = 0

    while stack:
        node = stack.pop()
        # do some logic
        for neighbor in graph[node]:
            if neighbor not in seen:
                seen.add(neighbor)
                stack.append(neighbor)
    
    return ans

# BFS

from collections import deque

def fn(graph):
    queue = deque(['START_NODE'])
    seen = {'START_NODE'}
    ans = 0

    while queue:
        node = queue.popleft()
        # do some logic
        for neighbor in graph[node]:
            if neighbor not in seen:
                seen.add(neighbor)
                queue.append(neighbor)
    
    return ans