import random

a = random.sample([_ for _ in range(100)],20)

def partition(a,low,high):
    pivot = a[low]
    leftmark = low+1
    rightmark = high

    while leftmark <= rightmark:
        while a[leftmark] < pivot and leftmark <= rightmark:
            leftmark += 1
        while a[rightmark] > pivot and rightmark >= leftmark:
            rightmark -= 1
        
        if leftmark > rightmark:
            break
        else:
            a[leftmark],a[rightmark] = a[rightmark],a[leftmark]
    
    a[low],a[rightmark] = a[rightmark],a[low]
    return rightmark

def quicksort(a,low,high):
    if low < high:
        p = partition(a,low,high)

        quicksort(a,low,p-1)
        quicksort(a,p+1,high)

quicksort(a,0,len(a)-1)

print(a)
