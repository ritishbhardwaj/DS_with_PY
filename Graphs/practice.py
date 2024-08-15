class node:
    def __init__(self,key):
        self.key=key
        self.next=None
class Stack:
    def __init__(self):
        self.head=None

    def is_empty(self):
        if self.head==None:
            return True
        else:
            return False

    def push(self,data):
        if self.head==None:
            self.head=node(data)
        else:
            v=node(data)
            v.next=self.head
            self.head=v
    def pop(self):
        if self.is_empty():
            return None
        else:
            print(self.head.key,  "is popped off")
            self.head=self.head.next

    def Print(self):
        t=self.head
        if self.is_empty():
            print("underflow")
            return
        else:
            while t:
                print(t.key,end=" ")
                t=t.next
            print()
stack_1=Stack()

class graph:
    def __init__(self,number_of_vertices,nature_graph):
        self.vert=number_of_vertices
        self.listOfLinks=[[] for i in range(self.vert)]
        self.nature=nature_graph

    def nature_grapgh(self):
        if self.nature == "U" or self.nature=="u":
            return True
        else:
            return False

    def add_edge(self,v=None,w=None):
        if self.nature_grapgh():
            if not(self.already_edge(v,w)):
                self.listOfLinks[v].append(w)
                self.listOfLinks[w].append(v)
        else:
            if not(self.already_edge(v,w)):
                self.listOfLinks[v].append(w)

    def remove_edge(self,v,w):
        if self.nature_grapgh():
            if self.already_edge(v,w):
                self.listOfLinks[v].remove(w)
                self.listOfLinks[w].remove(v)
        else:
                if self.already_edge(v,w):
                 self.listOfLinks[v].remove(w)
                else:
                    print("not Possible", v,w)    #test case (not important)

    def already_edge(self,v,w):
        if self.nature_grapgh():
            if (v in self.listOfLinks[w]) and (w in self.listOfLinks[v]):
                return True
            else:
                return False
        else:
            if w in self.listOfLinks[v]:
                return True
            else:
                return False

    def Print(self):
        for i in self.listOfLinks:
            print(i,end=" ")
        print()
#***in directed grph add_edge(1,2) means  edge or arrow going grom 1 to 2 i.e. |1| --> |2|  where 1 and 2 are vertices (and in technical term 2 has dependency over 1) ********
g=graph(5,"d")
graph_Property=["U","D"]   # U-> undirected    D->directed
g.add_edge(0,2)
g.add_edge(3,1)
g.add_edge(0,3)
g.remove_edge(3,0)
g.remove_edge(0,3)
g.Print()


