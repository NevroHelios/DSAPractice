def dijkstra_Mat(WMat: np.ndarray, s):
    rows, cols, x = WMat.shape
    infinity = WMat.max()*rows + 1
    visited, distance = {}, {}
    
    for v in range(rows):
        visited[v], distance[v] = False, infinity
    distance[s] = 0
    
    # computing sortest path for each vertex
    for u in range(rows):
        min_dist = min([distance[v] for v in range(rows) if not visited[v]]) 

        next_vlist = [v for v in range(rows) if not visited[v] and distance[v] == min_dist] # take vertises with min dist
        next_v = min(next_vlist) # vertix with min value

        visited[next_v] = True
        
        for v in range(cols): # for each neighbor of next_v
            if WMat[next_v, v, 0] == 1 and not visited[v]:
                if distance[next_v] + WMat[next_v, v, 1] < distance[v]:
                    distance[v] = distance[next_v] + WMat[next_v, v, 1]
    
    return distance


def dijkstra_list(WList: list, s):
    infinity = max(WList.keys()) * max([d for u in WList.keys() for k, d in WList[u]]) + 1
    visited, distance = {}, {}

    for i in range(len(WList)):
        visited[i], distance[i] = False, infinity
    
    distance[s] = 0
    
    for u in range(len(WList)):
        min_dist = min([distance[v] for v in range(len(WList)) if not visited[v]])
        next_vlist = [v for v in range(len(WList)) if  not visited[v] and distance[v] == min_dist]
        
        next_v = min(next_vlist)
        visited[next_v] = True
        
        for (v, d) in WList[next_v]:
            if not visited[v] and distance[next_v] + d < distance[v]:
                distance[v] = distance[next_v] + d
    
    return  distance



import numpy as np
dedges = [(0,1,10),(0,2,80),(1,2,6),(1,4,20),(2,3,70),(4,5,50),(4,6,5),(5,6,10)]
size = 7

# Adj Matrix
W = np.zeros(shape=(size, size, 2))
for (i, j , w) in dedges:
    W[i, j, 0] = 1
    W[i, j, 1] = w
print(dijkstra_Mat( W, 0))
    
# ADJ LIST
WL = {}
for i in range(size):
    WL[i] = []
for (i, j, d) in dedges:
    WL[i].append((j, d))
print(dijkstra_list(WL, 0))
