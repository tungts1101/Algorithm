import sys
from collections import defaultdict
from queue import LifoQueue
import heapq

class DirectedEdge:
    def __init__(self,v,w,weight):
        self.v = int(v)
        self.w = int(w)
        self.weight = weight

    def __repr__(self):
        return "{0}->{1} {2}".format(self.v,self.w,self.weight)

class EdgeWeightedDigraph:
    def __init__(self):
        self.V = 0
        self.E = 0
        self.adj = defaultdict(lambda: [])
    
    def insert(self,inp):
        f = open(inp,'r')
        self.V = int(f.readline())
        E = int(f.readline())
        
        for _ in range(E):
            v,w,weight = list(map(float,f.readline().split()))
            e = DirectedEdge(v,w,weight)
            self.addEdge(e)

    def addEdge(self,e: DirectedEdge):
        self.adj[e.v].append(e)
        self.E += 1

    def adjacents(self,v: int):
        return self.adj[v]

    def edges(self):
        return [e for v in range(self.V) for e in self.adj[v]]

MAX = sys.maxsize

class SP:
    def __init__(self,g,s):
        self.distTo = [MAX] * g.V
        self.distTo[s] = 0

        self.edgeTo = [None] * g.V

    def distTo(self,v):
        return self.distTo[v]

    def hasPathTo(self,v):
        return self.distTo[v] < MAX

    def pathTo(self,v):
        if not self.hasPathTo(v):
            return None
        path = LifoQueue()
        e = self.edgeTo[v]
        while e:
            path.put(e)
            e = self.edgeTo[e.v]

        return path

class PriorityQueue:
    def __init__(self,key):
        self.key = key
        self._q = []
    def enqueue(self,item):
        self._q.append(item)
        self._q.sort(key=self.key)
    def dequeue(self):
        return self._q.pop(0)
    def contains(self,item):
        return item[0] in set([x[0] for x in self._q])
    def update(self,item):
        for x in self._q:
            if x[0] == item[0]:
                x[1] = item[1]
                break
        self._q.sort(key=self.key)
    def empty(self):
        return len(self._q) == 0

class DijkstraSP(SP):
    def __init__(self,g,s):
        super().__init__(g,s)

        self.pq = PriorityQueue(key=lambda x:x[1])
        self.pq.enqueue((s, 0.0))
        while not self.pq.empty():
            self.relax(g, self.pq.dequeue()[0])

    def relax(self,g,v):
        for e in g.adjacents(v):
            w = e.w
            if self.distTo[w] > self.distTo[v] + e.weight:
                self.distTo[w] = self.distTo[v] + e.weight;
                self.edgeTo[w] = e
                item = (w, self.distTo[w])
                if self.pq.contains(item):
                    self.pq.update(item)
                else:
                    self.pq.enqueue(item)
