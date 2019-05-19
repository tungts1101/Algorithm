# https://www.geeksforgeeks.org/matrix-chain-multiplication-dp-8/

# top down approach
import sys

T = int(input())
N = [None] * T
A = [[]] * T

for i in range(T):
    N[i] = int(input())
    A[i] = list(map(int,input().split()))

for i in range(T):
    m = [[0 for col in range(N[i])] for row in range(N[i])]

    for L in range(2,N[i]):
        for j in range(1,N[i]-L+1):
            k = j+L-1
            m[j][k] = sys.maxsize

            for p in range(j,k):
                q = min(m[j][p],m[p+1][k]) + A[i][j-1]*A[i][p]*A[i][k]
                if q < m[j][k]:
                    m[j][k] = q

    print(m[1][N[i]-1])

# bottom up approach
# import sys

# T = int(input())
# N = [None] * T
# A = [[]] * T

# for i in range(T):
    # N[i] = int(input())
    # A[i] = list(map(int,input().split()))

# for i in range(T):
    # dp = {}
    
    # def mcm(j,k):
        # if (j,k) not in dp:
            # if j == k:
                # dp[(j,k)] = 0
            # else:
                # for p in range(j,k):
                    # dp[(j,k)] = min(mcm(j,p),mcm(p+1,k)) + A[i][j-1]*A[i][p]*A[i][k]
        
        # return dp[(j,k)]
    
    # print(mcm(1,N[i]-1))
