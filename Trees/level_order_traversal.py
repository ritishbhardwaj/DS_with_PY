from collections import deque
class node:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None
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
print('level order traversal is:',level_ord_traversal(root))
ans=level_ord_traversal(root)
for i in ans:
    i=deque(i)
    while len(i):
        print(i.popleft(),end=' ')
    print()
