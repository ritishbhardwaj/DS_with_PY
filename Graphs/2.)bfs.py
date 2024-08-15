
class graph:
    def __init__(self,vertices):
        self.listOflinks=[[] for i in range(vertices)]
        # print(self.listOflinks)

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

numberOfVertices=6
g1=graph(numberOfVertices)
g1.add_edge(0, 1)
g1.add_edge(0, 2)
g1.add_edge(1, 2)
g1.add_edge(2, 0)
g1.add_edge(2, 3)
g1.add_edge(3, 3)

g1.Print()
print()
# print()

from collections import deque
graph=g1.listOflinks    # list representation for graph
initialisation=2
visited=numberOfVertices*[0]   #created visited array and it has to be global
dq=deque()
def bfs(graph,v):
    u=v
    print(u,end=" ")
    visited[u]=1
    for w in graph[u]:
        # print(graph[u])    #not necessary, just for testing
        if visited[w]==0:
            dq.append(w)
            visited[w]=1
    if len(dq)==0:
        # print(dq)  #not necessary, just for testing
        return
    # print(visited)     #not necessary, just for testing
    # print(dq)
    u=dq.popleft()
    bfs(graph,u)

bfs(graph,initialisation)
print()
print(visited)