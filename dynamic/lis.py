# https://www.geeksforgeeks.org/longest-increasing-subsequence-dp-3/

T = int(input())
N = [0] * T
A = [[]] * T

for i in range(T):
    N[i] = int(input())
    A[i] = list(map(int,input().split()))

for i in range(T):
    arr = [1] * N[i]
    for j in range(N[i]):
        for k in range(0,j):
            if arr[j] <= arr[k] and A[i][k] < A[i][j]:
                arr[j] = arr[k] + 1

    print(max(arr))
