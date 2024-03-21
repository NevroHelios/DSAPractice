# Rope Cutting Problem

def maxpeices(n,a,b,c) :
    if n == 0 :
        return 0
    if n <= -1 :
        return -1 
    res = max(maxpeices(n-a,a,b,c),
              maxpeices(n-b,a,b,c),
              maxpeices(n-c,a,b,c))
    if res == -1 :
        return -1 
    return res + 1 
    
    
n = 23
a = 11
b = 9 
c = 12
print(maxpeices(n,a,b,c))