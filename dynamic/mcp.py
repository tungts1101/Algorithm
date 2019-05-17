# https://www.geeksforgeeks.org/min-cost-path-dp-6/

import sys

T = int(input())
N = [None] * T
M = [[]] * T
for i in range(T):
    N[i] = int(input())
    M[i] = list(map(int,input().split()))

for i in range(T):
    def idx(r,c):
        return r*N[i] + c
    
    cp = [[0 for c in range(N[i])] for r in range(N[i])]
    cp[0][0] = M[i][idx(0,0)]
    
    for r in range(1,N[i]):
        cp[r][0] = cp[r-1][0] + M[i][idx(r,0)]
    
    for c in range(1,N[i]):
        cp[0][c] = cp[0][c-1] + M[i][idx(0,c)]
    
    for r in range(1,N[i]):
        for c in range(1,N[i]):
            cp[r][c] = M[i][idx(r,c)] + min(cp[r][c-1],cp[r-1][c],cp[r-1][c-1])
    
    print(cp[N[i]-1][N[i]-1])
