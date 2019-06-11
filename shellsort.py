import random

a = random.sample([i for i in range(100)],26)

def shellsort(a):
    n = len(a)
    gap = n//2

    while gap > 0:
        for i in range(gap,n):
            tmp = a[i]
            j = i
            while j >= gap and a[j-gap] > tmp:
                a[j] = a[j-gap]
                j -= gap
            a[j] = tmp
        gap //= 2

shellsort(a)
print(a)
