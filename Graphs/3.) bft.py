'''we implement this when we have two or more disconnected graphs and in that situation we do traversal
So we do  BREADTH FIRST TRAVERSAL (BFT)'''

class graph:
    def __init__(self,vertices):
        self.listOflinks=[[] for i in range(vertices)]

    def add_edge(self,v,w):
        if self.already_attained_edge(v,w)==False:
            self.listOflinks[v].append(w)
            self.listOflinks[w].append(v)

    def already_attained_edge(self,v,w):
        if (w in self.listOflinks[v]) and (v in self.listOflinks[w]):
            return True
        else:
            return False

    def remove_edge(self,v,w):
        if self.already_attained_edge(v,w)==True:
            self.listOflinks[v].remove(w)
            self.listOflinks[w].remove(v)
        else:
            print("chal_hatt..... remove kar diya hua hai upar kisi step pe")
            print("bhai print kara ke dekh, farak dikhega")

    def Print(self):
        for i in self.listOflinks:
            print(i,end=" ")


numberOfVertices_1=6
g1=graph(numberOfVertices_1)
g1.add_edge(0,1)
g1.add_edge(0,2)
g1.add_edge(1,3)
g1.add_edge(1,5)
g1.add_edge(2,3)
g1.add_edge(4,5)
g1.add_edge(3,5)
g1.add_edge(1,2)

numberOfVertices_2=4
g2=graph(numberOfVertices_2)
g2.add_edge(0,1)
g2.add_edge(0,2)
g2.add_edge(1,3)
g2.add_edge(2,3)
g2.add_edge(3,2)
g2.add_edge(3,0)
g2.add_edge(1,2)

total_number_of_vertices=numberOfVertices_1 + numberOfVertices_2

from collections import deque
graph1=g1.listOflinks    # list representation for graph
graph2=g2.listOflinks    # list representation for graph
initialisation=5
visited=total_number_of_vertices*[0]   #created visited array and it has to be global
dq=deque()

def bft():pass

def bfs(graph,v):
    u=v
    print(u,end=" ")
    visited[u]=1
    for w in graph[u]:
        if visited[w]==0:
            dq.append(w)
            visited[w]=1
    if len(dq)==0:
        return
    # print(visited)
    u=dq.popleft()
    bfs(graph,u)

bfs(graph1,initialisation)
