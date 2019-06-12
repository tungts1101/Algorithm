from queue import Queue,LifoQueue

class DepthFirstOrder:
    def __init__(self,g):
        self.pre = Queue()
        self.post = Queue()
        self.reversePost = LifoQueue()

        self.marked = [False] * g.V
        for v in range(g.V):
            if not self.marked[v]:
                self.dfs(g,v)
            
    def dfs(self,g,v):
        self.pre.put(v)
        self.marked[v] = True
        for w in g.adjacents(v):
            if not self.marked[w]:
                self.dfs(g,w)
        self.post.put(v)
        self.reversePost.put(v)

class KosarajuCC:
    def __init__(self,g):
        self.marked = [False] * g.V
        self.id = [None] * g.V
        self.count = 0

        order = DepthFirstOrder(g.reverseGraph())
        while not order.reversePost.empty():
            s = order.reversePost.get()
            if not self.marked[s]:
                self.dfs(g,s)
                self.count += 1
        
        print(str(self.count) + " components")
        for c in range(self.count):
            for index,i in enumerate(self.id):
                if i == c:
                    print(index, end=' ')
            print()

    def dfs(self,g,v):
        self.marked[v] = True
        self.id[v] = self.count
        for w in g.adjacents(v):
            if not self.marked[w]:
                self.dfs(g,w)
