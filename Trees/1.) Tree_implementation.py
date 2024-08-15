class node:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None

def Inorder(t):
    if t:
        Inorder(t.left)
        print(t.key,end=" ")
        Inorder(t.right)
        return ""

def preorder(t):
    if t:
        print(t.key,end=" ")
        preorder(t.left)
        preorder(t.right)
        return ""

def PostOrder(t):
    if t:
        PostOrder(t.left)
        PostOrder(t.right)
        print(t.key,end=" ")
        return ""

root=node(100)
root.left=node(200)
root.right=node(300)
root.left.left=node(400)
root.left.right=node(500)
root.right.left=node(600)
root.right.right=node(700)

print(Inorder(root),"<--- INORDER")
print(preorder(root),"<--- PREORDER")
print(PostOrder(root),"<--- POSTORDER")





