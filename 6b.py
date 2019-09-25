class graph:
    def __init__(self,v):
        self.v=v
        self.adj=[[] for i in range(self.v)]
    def tops(self):
        indegree=[0]*self.v
        for i in range(self.v):
            for j in self.adj[i]:
                indegree[j]=indegree[j]+1
        q=[]
        for i in range(self.v):
            if indegree[i]==0:
                q.append(i)
        while q:
            a=q.pop()
            for i in self.adj[a]:
                indegree[i]-=1
                if indegree[i]==0:
                    q.append(i)
            print(a)

    def addedge(self,u,v):
        self.adj[u].append(v)
g=graph(5)
g.addedge(0,1)
g.addedge(0,2)
g.addedge(1,3)
g.addedge(2,3)
g.addedge(3,4)
g.tops()
                    
            
