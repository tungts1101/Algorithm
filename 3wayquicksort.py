import random

a = [[random.choice([_ for _ in range(20)])]*random.choice([_ for _ in range(8)]) for _ in range(8)]

a = [x for y in a for x in y]
random.shuffle(a)

def sort(arr,lo,hi):
    if lo < hi:
        lt,i,gt = lo,lo+1,hi
        v = arr[lo]
        while i <= gt:
            if arr[i] < v:
                arr[lt],arr[i] = arr[i],arr[lt]
                lt += 1;i += 1
            elif arr[i] > v:
                arr[gt],arr[i] = arr[i],arr[gt]
                gt -= 1
            else:
                i += 1

        sort(arr,lo,lt-1)
        sort(arr,gt+1,hi)

sort(a,0,len(a)-1)
print(a)
