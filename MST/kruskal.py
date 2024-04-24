def find(parent,i):
    if parent[i] == i:
        return i
    return find(parent,parent[i])

def union(parent,rank,x,y):
     x_root = find(parent,x)
     y_root = find(parent,y)
     if rank[x_root] < rank[y_root]:
         parent[x_root] = y_root
     elif rank[x_root] > rank[y_root]:
         parent[y_root] = x_root
     else:
        parent[y_root] = x_root
        rank[x_root] += 1
        
def kruskal(graph):
    sorted_edges = sorted(graph['edges'])
    print(sorted_edges)
    mst = []
    parent = {v : v for v in graph['vertices']}
    rank = {v : 0 for v in graph['vertices']}
    print("Parent: ",parent)
    print("Rank: ",rank)
    
    for weight,u,v in sorted_edges:
        u_parent = find(parent,u)
        v_parent = find(parent,v)
        
        if u_parent != v_parent:
            mst.append((weight,u,v))
            union(parent,rank,u_parent,v_parent)
        else:
            print("Rejectedd")
    return mst

graph = {
    'vertices' : ['A','B','C','D','E','F'],
    'edges' : [
        (7,'A','B'),(5,'A','D'),(8,'B','C'),(9,'B','D'),(7,'B','E'),(5,'C','E'),(6,'D','F'),(8,'E','F')
        ]
    }
mst = kruskal(graph)
mini_cost = 0
for edge in mst:
    mini_cost += edge[0]
print("Minimum cost : ",mini_cost)
