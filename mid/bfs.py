from queue import Queue

ver = int(input())
edg = int(input())

def graph(ver, edg):       
    adj_list = {}
    for i in range(ver):
        adj_list[i] = []
        
    for i in range(edg):
        v = int(input())
        u = int(input())
        adj_list[u].append(v)
        adj_list[v].append(u) 
          
    return adj_list

adj_list = graph(ver, edg)


def bfsOfGraph(ver, adj): 
    vis = [] * ver
    for i in range(ver):
        vis.append(False) 
    
    # bfs = []
    q = Queue()
    q.put(0)
    vis[0] = True
    
    while not q.empty() :
        node = q.get()
        # bfs.append(node)
        print(node)
        
        for v in adj[node]:
            if not vis[v]:
                vis[v] = True
                q.put(v)
        
        
print("BFS")
bfsOfGraph(ver, adj_list)      
        
        

    
    
    
    




    