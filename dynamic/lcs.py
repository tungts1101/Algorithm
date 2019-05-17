# https://www.geeksforgeeks.org/longest-common-subsequence-dp-4/

T = int(input())
n = [None] * T
m = [None] * T
A = [[]] * T
B = [[]] * T

for i in range(T):
    n[i],m[i] = list(map(int,input().split()))
    A[i] = input()
    B[i] = input()

for i in range(T):
    dp = [[None] * (m[i]+1) for j in range(n[i]+1)]
    
    for j in range(n[i]+1):
        for k in range(m[i]+1):
            if j == 0 or k == 0:
                dp[j][k] = 0
            else:
                if A[i][j-1] == B[i][k-1]:
                    dp[j][k] = dp[j-1][k-1] + 1
                else:
                    dp[j][k] = max(dp[j-1][k],dp[j][k-1])
    
    print(dp[n[i]][m[i]])
