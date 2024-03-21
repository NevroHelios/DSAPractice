import time

t = time.time()
def power(N,R):
    #Your code here
    ans = 1
    mod = 1000000007

    if R < 0:
        R = -R
        N = 1 / N

    while R > 0:
        if R % 2 == 1:
            ans = (ans * N) % mod
        N = (N * N) % mod
        R //= 2

    return ans

print(power(123456, 654321))
print(time.time()-t)