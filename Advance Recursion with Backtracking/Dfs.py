
# def dfs(visited, result, adj, node):
#     visited[node] = 1
#     result.append(node)
#     for i in adj[node]:
#         if visited[i] == 0:
#             dfs(visited, result, adj, i)








def dfs(adj, result, visited, node):
    visited[node] = 1
    result.append(node)
    for n in adj[node]:
        if visited[n] == 0:
            dfs(adj, result, visited, n)
        
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
nodes = 8
result = []
visited = [0] * ( nodes + 1 )

dfs(adj, result, visited, 1)
dfs(adj, result, visited, 1)

print(result)
