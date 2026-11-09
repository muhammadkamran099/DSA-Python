from collections import deque

def bfs(adj, n, start):
    queue = deque()
    visited = [0] * ( n + 1 )
    ans = []
    queue.append(start)
    visited[start] = 1
    





adjacency_list = [
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
