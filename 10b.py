def floyds(a,n):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                a[i][j]=min(a[i][j],(a[i][k]+a[k][j]))


    for i in range(len(a)):
        for j in range(len(a)):
            print(a[i][j],end=" ")
        print( )
a=[[0,2,999,1,8],
   [6,0,3,2,999],
   [999,999,0,4,999],
   [999,999,2,0,3],
   [3,999,999,999,0]]
floyds(a,5)
