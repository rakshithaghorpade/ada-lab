def quicksort(a,l,h):
	if l<h:
		ps=partition(a,l,h)
		quicksort(a,l,ps-1)
		quicksort(a,ps+1,h)
def partition(a,l,h):
	i,j=1+l,h
	while True:
		while a[l]>=a[i] and i<h:
			i=i+1
		while a[l]<a[j] and j>=l:
			j=j-1
		if(i<j):
			a[i],a[j]=a[j],a[i]
		else:
			a[l],a[j]=a[j],a[l]
			return j
l=list(map(int,input().split()))
quicksort(l,0,len(l)-1)
print(l)
