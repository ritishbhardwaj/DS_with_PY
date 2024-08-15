# class node:
#     def __init__(self,key):
#         self.key=key
#         self.left=None
#         self.right=None
#
# def count_number_of_nodes(root):
#     t=root
#     if t==None:
#         return 0
#     else:
#         l=count_number_of_nodes(t.left)
#         r=count_number_of_nodes(t.right)
#         return (1+l+r)
#
# def count_number_of_leaves(root):
#     t=root
#     if t==None:
#         return 0
#     elif t.left==None and t.right==None:
#         return 1
#     else:
#         l=count_number_of_leaves(t.left)
#         r=count_number_of_leaves(t.right)
#         return l+r
#
# def count_number_of_non_leaves(root):
#     t=root
#     if t==None:
#         return 0
#     elif t.left==None and t.right==None:
#         return 0
#     else:
#         l=count_number_of_non_leaves(t.left)
#         r=count_number_of_non_leaves(t.right)
#         return 1+l+r
#
# def count_full_nodes(root):
#     t=root
#     if t==None:
#         return 0
#     elif t.left==None and t.right==None:
#         return 0
#     else:
#         l=count_full_nodes(t.left)
#         r=count_full_nodes(t.right)
#         c= (1 if (t.left!=None and t.right!=None) else 0 )
#         return l+r+c
class node:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None
def inorder(root):
    t=root
    if t :
        inorder(t.left)
        print(t.key,end=' ')
        inorder(t.right)
        return
def preorder(root):
    t=root
    if t:
        print(t.key,end=' ')
        preorder(t.left)
        preorder(t.right)

def postorder(root):
    t=root
    if t:
        postorder(t.left)
        postorder(t.right)
        print(t.key,end=' ')

def level_ord_traversal(root):
    t=root
    if t==None:
        return
    queue=[]
    sub_ans=[]
    final_ans=[]
    final_ans.append([t.key])
    queue.append(t)
    while queue:
        l=len(queue)
        for turns in range(len(queue)):
            i=0
            if queue[i].left!=None :
                queue.append(queue[i].left)
                sub_ans.append(queue[i].left.key)
            if queue[i].right!=None:
                queue.append(queue[i].right)
                sub_ans.append(queue[i].right.key)
            queue.remove(queue[0])
        if sub_ans:
            final_ans.append(sub_ans)
        sub_ans=[]
    return final_ans

def count_nodes(root):
    t=root
    if t:
        l=count_nodes(t.left)
        r=count_nodes(t.right)
        return 1+l+r
    else:
        return 0

def number_of_leaves(root):
    t=root
    if t:
        if t.left== None and t.right==None:
            return 1
        else:
            l=number_of_leaves(t.left)
            r=number_of_leaves(t.right)
            return l+r
    else:
        return 0

def count_fullNodes(root):
    t=root
    if t== None:
        return 0
    elif t.left==None and t.right==None:
        return 0
    else:
        l_child=count_fullNodes(t.left)
        r_child=count_fullNodes(t.right)
        c=1 if (t.left!=None and t.right!=None) else 0
        return l_child+r_child+c

root=node(100)
root.left=node(200)
root.right=node(300)
root.left.left=node(400)
root.left.right=node(500)
root.right.left=node(600)
root.right.right=node(700)
root.right.right.left=node(800)
root.right.right.left.left=node(900)
root.right.right.left.right=node(1000)

print('inorder is:',end=' ')
inorder(root)
print()
print('preorder is:',end=' ')
preorder(root)
print()
print('postorder is:',end=' ')
postorder(root)
print()
print('level order traversal is:',level_ord_traversal(root))
# print()
print('number of nodes:',count_nodes(root))
print('number of leaves:',number_of_leaves(root))
print(count_fullNodes(root))

# print(count_number_of_nodes(root),"<-- number of nodes")
# print(count_number_of_leaves(root),"<--- number of leaves")
# print(count_number_of_non_leaves(root),"<-- number of non-leaves")
# print(count_full_nodes(root),"<--- number of full nodes")
