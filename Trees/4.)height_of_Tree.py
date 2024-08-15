class node:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None

def height_Tree(root):
    t=root
    if t==None:
        return 0
    elif t.left==None and t.right==None :
        return 0
    else:
        l=height_Tree(t.left)
        r=height_Tree(t.right)
        ans= l if l>r else r
        return 1+ans

root=node(100)
root.left=node(200)
root.right=node(300)
root.left.left=node(400)
root.left.right=node(500)
root.right.left=node(600)
root.right.right=node(700)
root.right.right.left=node(700)
root.right.right.left.left=node(700)
root.right.right.left.right=node(700)
a=root.right.right.left.left.right=node(700)
a.right=node(800)

print(height_Tree(root))
print(root.left.right)