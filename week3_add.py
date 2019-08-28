def merge(l1,l2):
        a=[]
        i,j,k=0,0,0
        while i<len(l1) and j<len(l2):
            if l1[i]<l2[j]:
                a.append(l1[i])
                i=i+1
            else:
                a.append(l2[j])
                j=j+1
        while i<len(l1):
            a.append(l1[i])
            i=i+1
        while j<len(l2):
            a.append(l2[j])
            j=j+1
        return a
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
l=merge(l1,l2)
m=(len(l)-1)//2
median=(l[m]+l[m+1])/2
print("median :",median)
