'''from dataclasses import dataclass
pair=[]
@dataclass
class Pair:
    first:eval
    second:eval

# tuple=[(1,2),(2,3)]
# a=Pair(True,0)
# ans=Pair       # ans has a data type as Pair now
# ans.first=10
# print(ans.first)
# print(type(ans))
# print(a.first,a.second)

class node:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None
def isbalancedTree(root):
    if root==None:
        p=Pair(True,0)

        return p
    left=Pair
    right=Pair
    left=isbalancedTree(root.left)
    right=isbalancedTree(root.right)
    leftAns=left.first
    rightAns=right.first
    diff=abs(left.second-right.second)<=1
    ans=Pair
    ans.second=max(left.second,right.second)+1
    if leftAns and rightAns and diff:
        ans.first=True
    else:
        ans.first=False
        '''
class node:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None

def isbalancedTree(root):
    if root==None:
        return 0
    elif root.left==None and root.right==None:
        return 0
    else:
        l=isbalancedTree(root.left)

        r=isbalancedTree(root.right)
        if l == -1: return -1
        if r==-1 :return -1
        if abs(l-r)>1 : return -1
        # if l == -1: return -1
        # if r==-1 :return -1
        print(l, '--', r)
        return 1+max(l,r)
# root=node(100)
# root.left=node(200)
# root.right=node(300)
# root.left.left=node(400)
# root.left.right=node(500)
# root.right.left=node(600)
# root.right.right=node(700)
# root.right.right.left=node(800)
# root.right.right.left.left=node(900)
# root.right.right.left.right=node(1000)
# a=root.right.right.left.left.right=node(1100)
# a.right=node(1200)
root=node(1)
root.right=node(2)
root.right.right=node(3)
ans=isbalancedTree(root)
print(ans)