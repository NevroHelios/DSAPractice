
def re_fibo(n):
    if n <= 2:
        return 1
    return re_fibo(n-1) + re_fibo(n - 2)

def fibo(n, dp):
    if n <= 2:
        return 1
    if dp[n] != 0:
        return dp[n]
    dp[n] = fibo(n-1, dp) + fibo(n-2, dp)
    return dp[n]

def dp_fibo(n):
    
    lis = [0 for _ in range(n + 1)]
    lis[1] = 1
    lis[2] = 1
    for i in range(3, n + 1):
        lis[i] = lis[i - 1] + lis[i - 2]
        
    return lis[n]

def op_fibo(n):
    lis = [-1, 1, 1, 0]
    if n <= 2:
        return 1
    for i in range(2, n):
        lis[3] = lis[1] + lis[2]
        lis[1] = lis[2]
        lis[2] = lis[3]
    return lis[3]

n = 9

print(re_fibo(n)) # Output:  34
print(fibo(n, [0]*(n+1))) # Output: 34
print(dp_fibo(n)) # Output:  34
print(op_fibo(n))

# print([2]*7)