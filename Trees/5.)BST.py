class node:
    def __init__(self,key=None):
        self.key=key
        self.left=None
        self.right=None
def levelOrderTreversal(root):
    if root==None:
        return None
    que=[]
    que.append(root)
    while que:
        processedRoot=que.pop(0)
        print(processedRoot.key, end=" ")
        if processedRoot:
            if processedRoot.left:
                que.append(processedRoot.left)
            if processedRoot.right:
                que.append(processedRoot.right)

def insert_inBst(root,data):    #----------------> TC::O(log(n))    SC::O(log(n))
    if root.key==None:
        root.key=data
    elif data<=root.key:
        if root.left==None:
            root.left=node(data)
        else:
            insert_inBst(root.left,data)
    else:
        if root.right==None:
            root.right=node(data)
        else:
            insert_inBst(root.right,data)
    return f"{data} node has been succesfully inserted to tree"

def search(root,data):
    if root.key==data:
        return f'{data} is successfully found in BST'
    elif data<root.key:
        if root.left:
            Lans=search(root.left,data)
            return Lans
        else:
            return 'not found'
    else:
        if root.right:
            Rans=search(root.right,data)
            return Rans
        else:
            return 'not found'

def deletenode(root,data):   #-----------------------> O(log(n))
    if root==None:
        return None
    elif root.key>data:
        root.left=deletenode(root.left,data)
    elif root.key<data:
        root.right=deletenode(root.right,data)
    else:

        if root.right!=None and root.left!=None:
            mx = findmax(root.left)
            root.key=mx
            root.left=deletenode(root.left,mx)

        elif root.left!=None:
            return root.left
        elif root.right!=None:
            return root.right
        else:
            return None
    return root       # most important step is this to return the root [ONLY CAN BE CLEARED WHEN DRAW RECURSIVE TREE]  ///KNOW one thing if we dont return then function return None by default
                    # So where ever is the deletenode() vala function if we do not return then by default it is None value which means at line 54. value of root.left will become None .
                        # Ok so no explanation further, make a normal recursive tree and then i will know everything\





def findmax(root):
    if root.right==None:
        return root.key
    ans=findmax(root.right)
    return ans

def deleteBST(root):
    root.right=None
    root.left=None


newBST=node()
# print(newBST.key)
print(insert_inBst(newBST,70))
print(insert_inBst(newBST,50))
print(insert_inBst(newBST,90))
print(insert_inBst(newBST,30))
print(insert_inBst(newBST,80))
print(insert_inBst(newBST,60))
print(insert_inBst(newBST,100))
print(insert_inBst(newBST,20))
print(insert_inBst(newBST,40))
print(insert_inBst(newBST,55))
# print(newBST.key)
# print(newBST.left.key)
# print(newBST.right.key)
# print(newBST.right.left.key)
# # print(newBST.right.left.right.key)
print('----------------------------')
levelOrderTreversal(newBST)
print()
print(search(newBST,20))
print('==============>',newBST.left.right.left.key)

# newBST=deletenode(newBST,50)
deletenode(newBST,50)
levelOrderTreversal(newBST)
# print(findmax(newBST),'<============')
