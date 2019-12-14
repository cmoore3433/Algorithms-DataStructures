import queue
from collections import OrderedDict
from math import inf
class GraphNode:
    def __init__(self, key):
        self.key=key
        self.predecessor=None
        self.color=None
        self.distance=None
        self.f=0
        self.fweight=0
    def __lt__(self, other):
        return self.fweight < other.fweight

class GraphEdge:
    def __init__(self, weight, endNode):
        self.weight=weight
        self.endNode=endNode
    def __lt__(self, other):
        return self.weight < other.weight

class Graph:
    def __init__(self):
        d={}
        self.graph=OrderedDict(d.items())
        self.dfstime=0
        self.topGraph=[]
        
    def addNode(self, u):
        self.graph[u]=queue.PriorityQueue()
    
    def addEdge(self, u, v, w=0):
        if u in self.graph:
            self.graph[u].put(GraphEdge(w,v))
        else:
            self.addNode(u)
            self.graph[u].put(GraphEdge(w,v))
        if v in self.graph:
            self.graph[v].put(GraphEdge(w,u))
        else:
            self.addNode(v)
            self.graph[v].put(GraphEdge(w,u))
    
    def bfs(self, node):
        for u in self.graph:
            u.color="White"
            u.distance=0
            u.predecessor=None
        node.color="Gray"
        node.distance=0
        node.predecessor=None
        Q=queue.Queue()
        Q.put(node)
        while Q.empty()!=True:
            u=Q.get()
            temp=[]
            while self.graph[node].empty()!=True:
                temp.append(self.graph[node].get())
            for v in temp:
                if v.endNode.color=="White":
                    v.endNode.color="Gray"
                    v.endNode.distance=u.distance+1
                    v.endNode.predecessor=u
                    self.graph[node].put(v)
            u.color="Black"
            
    def printPath(self, s, v, first=True):
        if v==s:
            print(s.key)
        elif v.predecessor is None and first==False:
            return
        elif v.predecessor is None:
            print("No path between the two nodes.")
        else:
            self.printPath(s, v.predecessor, False)
            print(v.key)

    def dfs(self):
        for u in self.graph:
            u.color="White"
            u.predecessor=None
        self.dfstime=0
        for u in self.graph:
            if u.color=="White":
                self.dfsVisit(u)
        
    def dfsVisit(self, node):
        self.dfstime=self.dfstime+1
        node.distance=self.dfstime
        node.color="Gray"
        Q=queue.Queue()
        Q.put(node)
        while Q.empty()!=True:
            u=Q.get()
            temp=[]
            while self.graph[node].empty()!=True:
                temp.append(self.graph[node].get())
            for v in temp:
                self.graph[node].put(v)
                if v.endNode.color=="White":
                    v.endNode.predecessor=u
                    self.dfsVisit(v.endNode)
            node.color="Black"
            self.dfstime=self.dfstime+1
            node.f=self.dfstime
            self.topGraph.append(node.key)
        
    def topologicalSort(self):
        self.topGraph=[]
        self.dfs()
        self.topGraph.reverse()
        return self.topGraph

    def mstPrim(self,r):
        for u in self.graph:
            u.fweight=inf
            u.predecessor=None
        r.fweight=0
        Q=queue.PriorityQueue()
        for u in self.graph:
            Q.put(u)
        while Q.empty()!=True:
            u=Q.get()
            temp=[]
            while self.graph[u].empty()!=True:
                temp.append(self.graph[u].get())
            for v in temp:
                self.graph[u].put(v)
                if v.endNode in Q.queue and v.weight < v.endNode.fweight:
                    v.endNode.predecessor=u
                    v.endNode.fweight=v.weight
            
            
            