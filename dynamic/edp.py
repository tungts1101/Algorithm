# https://www.geeksforgeeks.org/egg-dropping-puzzle-dp-11/

# dynamic approach
# import sys

# T = int(input())
# N = [None] * T
# K = [None] * T

# for i in range(T):
    # N[i],K[i] = list(map(int,input().split()))

# def eggDrop(n,k):
    # eggFloor = [[0 for col in range(k+1)] for row in range(n+1)]
    
    # for i in range(1,n+1):
        # eggFloor[i][0] = 0
        # eggFloor[i][1] = 1
    
    # for j in range(1,k+1):
        # eggFloor[1][j] = j
    
    # for i in range(2,n+1):
        # for j in range(2,k+1):
            # eggFloor[i][j] = sys.maxsize
            # for x in range(1, j+1): 
                # res = 1 + max(eggFloor[i-1][x-1], eggFloor[i][j-x]) 
                # if res < eggFloor[i][j]: 
                    # eggFloor[i][j] = res
    
    # return eggFloor[n][k]

# for i in range(T):
    # print(eggDrop(N[i],K[i]))

# binomials approach


