import random

a = random.sample([_ for _ in range(100)],26)

def countingSort(arr,exp):
    n = len(arr)

    output = [0] * n
    count = [0] * 10    # base 10

    for i in range(n):
        index = arr[i]//exp
        count[(index%10)] += 1

    for i in range(1,10):
        count[i] += count[i-1]

    i = n-1
    while i >= 0:
        index = arr[i]//exp
        output[count[(index%10)]-1] = arr[i]
        count[(index%10)] -= 1
        i -= 1

    i = 0
    for i in range(n):
        arr[i] = output[i]

def radixsort(arr):
    _max = max(arr)
    exp = 1
    while _max/exp:
        countingSort(arr,exp)
        exp *= 10

radixsort(a)
print(a)
