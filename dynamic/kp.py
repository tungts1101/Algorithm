# https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/

T = int(input())
N = [None] * T
W = [None] * T
w = [[]] * T
v = [[]] * T

for i in range(T):
    N[i] = int(input())
    W[i] = int(input())
    w[i] = list(map(int,input().split()))
    v[i] = list(map(int,input().split()))
    
def knapsack(_W,_w,_v,_n):
    dp = [[0 for col in range(_W+1)] for row in range(_n+1)]
    
    for i in range(1,_n+1):
        for w in range(1,_W+1):
            if _w[i-1] > w:
                dp[i][w] = dp[i-1][w]
            else:
                dp[i][w] = max(dp[i-1][w],dp[i-1][w-_w[i-1]]+_v[i-1])
    
    return dp[_n][_W]

for i in range(T):
    print(knapsack(W[i],w[i],v[i],N[i]))
