class node:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None

def Firstfunc(t):
    if t:
        print(t.key,end=" ")
        Seconffunc(t.left)
        Seconffunc(t.right)
def Seconffunc(t):
    if t:
        Firstfunc(t.left)
        print(t.key,end=" ")
        Firstfunc(t.right)


root=node(100)
root.left=node(200)
root.right=node(300)
root.left.left=node(400)
root.left.right=node(500)
root.right.left=node(600)
root.right.right=node(700)

Seconffunc(root)
print()
Firstfunc(root)
print()

