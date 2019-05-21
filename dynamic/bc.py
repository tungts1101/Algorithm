# https://www.geeksforgeeks.org/binomial-coefficient-dp-9/
T = int(input())
n = [None] * T
r = [None] * T

for i in range(T):
    n[i],r[i] = list(map(int,input().split()))

for i in range(T):
    if r[i] > n[i]:
        print(0)
    else:
        dp = {}
        for j in range(n[i]+1):
            if j == 0 or j == 1:
                dp[j] = 1
            else:
                dp[j] = dp[j-1] * j
        
        print ((dp[n[i]]//(dp[r[i]] * dp[n[i] - r[i]])) % (10**9 + 7))
