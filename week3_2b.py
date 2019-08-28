

def bubble(arr):
    print("bubble sort \n")
    c=0
    for i in range(len(arr)):
        for j in range(len(arr)-1-i):
            c=c+1
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    print(arr)
    print(c)
    print("merge sort \n")


def merge(l):
    c=0
    if len(l)>1:
        m=len(l)//2
        l1=l[:m]
        l2=l[m:]
        merge(l1)
        merge(l2)
        i,j,k=0,0,0
        while i<len(l1) and j<len(l2):
            if l1[i]<l2[j]:
                l[k]=l1[i]
                i=i+1
            else:
                l[k]=l2[j]
                j=j+1
            k=k+1
        while i<len(l1):
            l[k]=l1[i]
            i=i+1
            k=k+1
        while j<len(l2):
            l[k]=l2[j]
            j=j+1
            k=k+1


def selection(arr):
    c=0
    print("selection: \n")
    for i in range(len(arr)):
        min=i
        for j in range(i+1,len(arr)):
            c=c+1
            if arr[j]<arr[min]:
                min=j
            arr[i],arr[min]=arr[min],arr[i]
    print(arr)
    print(c)

arr=list(map(int,input().split()))
bubble(arr)
merge(arr)
print(len(arr)-1)
selection(arr)

