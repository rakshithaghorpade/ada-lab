d=list(map(int,input().split()))

A=int(input())

c=[0]*(A+1)

s=[0]*(A+1)

for p in range(1,len(c)):

    m=100

    for i in range(len(d)):

        if d[i]<=p:

            if 1+c[p-d[i]]<m:

                m=1+c[p-d[i]]

                s[p]=i+1

    c[p]=m

a=A

while True:

    if a>0:

        print(d[s[a]-1])

    else:

        break

    a=a-d[s[a]-1]
