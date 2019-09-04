class Graph:
    def __init__(self,v):
        self.v=v
        self.adj=[[] for i in range(v)]
    def dfs(self,temp,v,visited):
        visited[v]=True
        temp.append(v)
        for i in self.adj[v]:
            if visited[i]==False:
                temp=self.dfs(temp,i,visited)
        return temp
    def add(self,v,w):
        self.adj[v].append(w)
        self.adj[w].append(v)
    def connect(self):
        visited=[]
        cc=[]
        for i in range(self.v):
            visited.append(False)
        for v in range(self.v):
            if visited[i]==False:
                temp=[]
                cc.append(self.dfs(temp,v,visited))
        return cc

g=Graph(5);
g.add(1,0)
g.add(2,3)
g.add(3,4)
cc=g.connect()
print("these are the connected components")
print(cc)
