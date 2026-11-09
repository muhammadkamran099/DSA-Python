
def dfs(visited, result, adj, node):
    visited[node] = 1
    result.append(node)
    for i in adj[node]:
        if visited[i] == 0:
            dfs(visited, result, adj, i)





adj = [
    [],
    [2, 4],
    [1, 3, 6],
    [2],
    [1, 5, 7],
    [4, 8],
    [2],
    [4, 3],
    [5, 7]
    
]
n = 8
result = []
visited = [0] * ( n + 1 )

dfs(visited, result, adj, 1)

print(result)
