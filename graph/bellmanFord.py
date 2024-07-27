import numpy as np

def bellmanford_Mat(WMat: np.ndarray, s):
    rows, cols, x = WMat.shape
    infinity = WMat.max() * rows + 1
    negcycle = False
    
    
    distance = {}
    for i in range(rows):
        distance[i] = infinity
    distance[s] = 0
    
    for i in range(rows):
        for v in range(rows):
            for u in range(cols):
                if WMat[v, u, 0] == 1:  # if there is an edge from v to u
                    if distance[u] > WMat[v, u, 1] + distance[v]:
                        distance[u] = distance[v] + WMat[v, u, 1]
    
    # if not negcycle:
    return distance


def bellmanford_List(WL, s):
    # implement the same algorithm as above but for a list of edges
    infinity = max(d for u in WL.keys() for k, d in WL[u])
    
    distace = {}
    for i in range(len(WL)):
        distace[i] = infinity
    distace[s] = 0
    
    for _ in range(len(WL)):
        for u in WL.keys():
            for v, w in WL[u]:
                if distace[v] > distace[u] + w:
                    distace[v] = w + distace[u]
    return distace


edges = [(0,1,10),(0,7,8),(1,5,2),(2,1,1),(2,3,1),(3,4,3),(4,5,-1),(5,2,-2),(6,1,-4),(6,5,-1),(7,6,1)]
size = 8 #len(edges) - 1
W = np.zeros(shape=(size, size, 2))

for (i, j, w) in edges:
    W[i, j, 0] = 1
    W[i, j, 1] = w
    
# print(W[0][0][0])
print(bellmanford_Mat(W, 0))

WL = {}
for i in range(size):
    WL[i] = []
for (i, j, d) in edges:
    WL[i].append((j, d))

# print(WL)
print(bellmanford_List(WL, 0))