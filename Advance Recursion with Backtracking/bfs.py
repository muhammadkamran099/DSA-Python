from collections import deque

def bfs(adj, n, start):
    queue = deque()
    visited = [0] * ( n + 1 )
    ans = []
    queue.append(start)
    visited[start] = 1
    while len(queue) != 0:
        e = queue.popleft()
        ans.append(e)
        for node in adj[e]:
            if visited[node] == 0:
                visited[node] = 1
                queue.append(node)
    return ans





adj = [
    [],
    [2, 8],
    [1, 3, 4],
    [2],
    [2, 5],
    [4, 6],
    [5, 7],
    [6, 8],
    [1, 7, 9],
    [8]
    
]

n = 9

print(bfs(adj, n, 1))
