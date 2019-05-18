# https://www.geeksforgeeks.org/coin-change-dp-7/

T = int(input())
M = [None] * T
A = [[]] * T
N = [None] * T

for i in range(T):
    M[i] = int(input())
    A[i] = list(map(int,input().split()))
    N[i] = int(input())
    
for i in range(T):
    dp = {}
    
    def count(m,n):
        if (m,n) not in dp:
            if n == 0:
                dp[(m,n)] = 1
            elif n < 0 or (m <= 0 and n >= 1):
                dp[(m,n)] = 0
            else:
                dp[(m,n)] = count(m-1,n) + count(m,n-A[i][m-1])
        
        return dp[(m,n)]
    
    print(count(M[i],N[i]))
