# https://www.geeksforgeeks.org/longest-palindromic-subsequence-dp-12/

# O(n^2) space auxiliary
def lps(s):
    n = len(s)
    L = [[0 for x in range(n)] for x in range(n)]

    for i in range(n):
        L[i][i] = 1
    
    # sl is subsequence length
    for sl in range(2,n+1):
        for i in range(n-sl+1):
            j = i+sl-1  # subsequence starts from i and ends in j
            if s[i] == s[j] and sl == 2:
                L[i][j] = 2
            elif s[i] == s[j]:
                L[i][j] = L[i+1][j-1] + 2
            else:
                L[i][j] = max(L[i][j-1],L[i+1][j])

    return L[0][n-1]

# O(n) space auxiliary
def _lps(s):
    n = len(s)
    # a[i] stores length of longest substring prefix ending with i
    a = [0] * n
    
    for i in range(n-1,-1,-1):
        tmp = 0
        for j in range(i,n):
            if i == j:
                a[i] = 1
            elif s[i] == s[j]:
                a[j],tmp = tmp+2,a[j]
            else:
                tmp = a[j]
                a[j] = max(a[j-1],a[j])

    return a[n-1]

seq = "GEEKS FOR GEEKS"
n = len(seq)
print(lps(seq))
print(_lps(seq))
