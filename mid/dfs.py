

def dfs(node, adj_list, vis):
    vis[node] = True
    print(node)
    
    for v in adj_list[node]:
        if not vis[v]:
            dfs(v, adj_list, vis)
    
    


ver = int(input())
edg = int(input())

vis = [] * ver
for i in range(ver):
    vis.append(False)
        
adj_list = {}
for i in range(ver):
    adj_list[i] = []
    
for i in range(edg):
    v = int(input())
    u = int(input())
    adj_list[u].append(v)
    adj_list[v].append(u) 
          

print("DFS")
dfs(0,adj_list, vis)