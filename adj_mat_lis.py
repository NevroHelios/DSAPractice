import numpy as np
dedges = [(0,1,10),(0,2,80),(1,2,6),(1,4,20),(2,3,70),(4,5,50),(4,6,5),(5,6,10)]

size = len(dedges) - 1

## Adj Matrix
W = np.zeros(shape=(size, size, 2))
# print(w[0])
for (i, j, w) in dedges:
    W[i, j, 0] = 1
    W[i, j, 1] = w
    
# print(W)

## Adj lIST
WL = {}
for (i, j, w) in dedges:
    WL.get(i, []).append((j, w))
    
print(WL)