import random

a = random.sample([i for i in range(100)],26)

# n: total number of nodes
# i: index of current node
def heapify(a,n,i):
    largest = i
    l = 2*i + 1
    r = 2*i + 2

    if l < n and a[l] > a[largest]:
        largest = l
    if r < n and a[r] > a[largest]:
        largest = r
    
    # if largest is not i
    if largest is not i:
        a[i],a[largest] = a[largest],a[i]
        heapify(a,n,largest)

# heap sort
def heapSort(a):
    n = len(a)

    for i in range(n//2-1,-1,-1):
        heapify(a,n,i)

    for i in range(n-1,-1,-1):
        a[0],a[i] = a[i],a[0]
        heapify(a,i,0)

heapSort(a)
print(a)
