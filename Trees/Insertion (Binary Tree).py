class node:
    def __init__(self,value):
        self.key=value
        self.left=None
        self.right=None
def inorder(root):
    if root:
        inorder(root.left)
        print(root.key,end=" ")
        inorder(root.right)


def levelOrderTreversal(root):

    queue=[]
    queue.append(root)
    while queue:
        processedRoot=queue.pop(0)
        if processedRoot:
            queue.append(processedRoot.left)
            queue.append(processedRoot.right)
            print(processedRoot.key,end=" ")


def insertNodeBT(rootnode,newNode):
    if not rootnode:
        rootnode= newNode

    else:pass


root=node(100)
root.left=node(200)
root.right=node(300)
root.left.left=node(400)
root.left.right=node(500)
root.right.left=node(600)
root.right.right=node(700)
# root.right.right.right=node(800)
# root.right.right.left=node(900)

inorder(root)
print()
levelOrderTreversal(root)