from collections import defaultdict

class Graph:
    def __init__(self):
        self.V = 0
        self.E = 0
        self.adj = defaultdict(lambda: [])

    def insert(self,inp):
        f = open(inp,'r')
        self.V = int(f.readline())
        self.E = int(f.readline())
        for _ in range(self.E):
            v,w = list(map(int,f.readline().split()))
            self.addEdge(v,w)

    def addEdge(self,v,w):
        self.adj[v].append(w)

    def adjacents(self,v):
        return self.adj[v]

    def reverseGraph(self):
        rGraph = Graph()
        rGraph.V = self.V
        rGraph.E = self.E

        for v in range(self.V):
            for w in self.adj[v]:
                rGraph.addEdge(w,v)

        return rGraph
