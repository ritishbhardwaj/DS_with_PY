# '''     LIST REPRESENTATION OF GRAPH  (W/O  OOPs)   '''
#
# def addEdge(adj,u,w):
#     adj[u].append(w)
#     adj[w].append(u)
#                         #because it is undirected graph so for first case 0->1 and 1->0 i.e. 0 has an edge with 1
#                         #and 1 has an edge with 0
#
# def print_gragh(adj):
#     for i in adj:
#         print(list(set(i)))
#
# v=4        # v is total number of vertices in a graph
# adj=[[] for i in range(v)]   # created a list containing sublist of links to each node
#                              # adj will be shown as -->  [[],[],[],[]]   when v is 4
#
# addEdge(adj,0,1)  #[[1],[0],[],[]]
# addEdge(adj,0,2)  #[[1,2],[0],[0],[]]
# addEdge(adj,1,2)  #[[1,2],[0,2],[0,1],[]]
# addEdge(adj,1,3)  #[[1,2],[0,2,3],[0,1],[1]]
# addEdge(adj,0,1)
# print(adj)
# print()
# print_gragh(adj)
# ###
# #
# #===============================================================================================================================================
#
# '''     LIST REPRESENTATION OF GRAPH  (With OOPs)   '''
#
#
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

numberOfVertices=9
g1=graph(numberOfVertices)
g1.add_edge(1,3)
g1.add_edge(1,5)
g1.add_edge(1,6)
g1.add_edge(1,5)
g1.add_edge(3,5)

g1.Print()
print()
g1.remove_edge(1,3)
# g1.remove_edge(1,3)
g1.Print()



# class graph:
#     def __init__(self,vertices):
#         self.vertices=vertices
#         self.adj_matrix= [[0 for i in range(vertices)] for j in range(vertices)]
#
#     def add_edge(self,v,w):
#         self.adj_matrix[v][w]=1
#         self.adj_matrix[w][v]=1
#
#     def remove_edge(self,v,w):
#         self.adj_matrix[v][w]=0
#         self.adj_matrix[w][v]=0
#
#
# g=graph(5)
# g.add_edge(1,3)
# g.add_edge(1,4)
# print(g.adj_matrix)