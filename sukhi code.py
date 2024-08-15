from queue import Queue
import array

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None




def preOrderTraversal(rootNode):
    if not rootNode:  # -------------->O(1)
        return
    print(rootNode.data)  # -------------->O(1)
    preOrderTraversal(rootNode.leftChild)  # -------------->O(n/2)
    preOrderTraversal(rootNode.rightChild)  # -------------->O(n/2)



def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)  # -------------->O(n/2)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)  # -------------->O(n/2)




def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)  # -------------->O(n/2)
    postOrderTraversal(rootNode.rightChild)  # -------------->O(n/2)
    print(rootNode.data)




def levelOrderTraversal(rootNode):
    if rootNode is None:
        return
    else:
        Q = Queue()
        Q.put(rootNode)
        while not (Q.empty()):
            node = Q.get()
            if node == None:
                continue
            print(node.data)
            Q.put(node.leftChild)
            Q.put(node.rightChild)




def search(root, value):
    if root is None:
        print("Tree doesnot exist")
    else:
        q = Queue()
        q.put(root)
        while not (q.empty()):
            rs = q.get()
            if value == rs.data:
                print(f"Successfully found {value}")
                break
            if rs.leftChild is not None:
                q.put(rs.leftChild)
            if rs.rightChild is not None:
                q.put(rs.rightChild)
        else:
            print(f"{value} Not found")




def insert(rootNode, newNode):
    if not rootNode:
        print("Tree is empty")
    else:
        q = Queue()
        q.put(rootNode)
        while not (q.empty()):
            rs = q.get()
            if rs.leftChild is not None:
                q.put(rs.leftChild)
            else:
                rs.leftChild = newNode
                print(f"Successfully inserted {newNode.data}")
                break
            if rs.rightChild is not None:
                q.put(rs.rightChild)
            else:
                rs.rightChild = newNode
                print(f"Successfully inserted {newNode.data}")
                break




def deepestNode(root):
    if not root:
        print('Tree not present')
    else:
        q = Queue()
        q.put(root)
        # deepestnode=[]
        # deepestnode.append(root)
        while not q.empty():
            rs = q.get()
            if rs.leftChild is not None:
                q.put(rs.leftChild)
                # deepestnode.append(rs.leftChild)
            if rs.rightChild is not None:
                q.put(rs.rightChild)
                # deepestnode.append(rs.rightChild)
        dpNode = rs
        return dpNode


def deleteNode(rootNode, dpn):
    if not rootNode:
        print('Tree doesNot exist')
    else:
        q = Queue()
        q.put(rootNode)
        while not (q.empty()):
            root = q.get()
            if root.data == dpn.data:
                # print(f"Successfully deleted {root.data}")
                root = None
                return
            if root.leftChild:
                if root.leftChild.data == dpn.data:
                    print(f"Successfully deleted {root.leftChild.data}")
                    root.leftChild = None
                    return
                else:
                    q.put(root.leftChild)
            if root.rightChild:
                if root.rightChild.data == dpn.data:
                    print(f"Successfully deleted {root.rightChild.data}")

                    # ans=root.rightChild.data
                    root.rightChild = None
                    return
                else:
                    q.put(root.rightChild)



# print(f"Successfully deleted {dpn}")

def delete(rootNode, node):
    t=rootNode
    if not rootNode:
        print('Tree not present')
    else:
        q = Queue()
        q.put(rootNode)
        dpn = deepestNode(rootNode)
        temp=dpn.data
        while not (q.empty()):
            root = q.get()
            if root.data == node:
                deleteNode(t,deepestNode(rootNode))
                root.data = temp
                print(f"The node has been successfully deleted {root.data}")

                return
            if root.leftChild is not None:
                q.put(root.leftChild)
            if root.rightChild is not None:
                q.put(root.rightChild)


def deleteTree(root):
    if not root:
        print("tree not present")
    else:
        q = None
        root.data = None
        root.leftChild = None
        root.rightChild = None
        print("Successfully deleted Tree")

newBt = TreeNode("Drinks")  # -------------->O(1)
hot = TreeNode("Hot")
cold = TreeNode("Cold")
newBt.leftChild = hot
newBt.rightChild = cold
tea = TreeNode("Tea")
coffee = TreeNode('Coffee')
hot.leftChild = tea
hot.rightChild = coffee
cola = TreeNode('Cola')
fanta = TreeNode("Fanta")
cold.leftChild = cola
cold.rightChild = fanta

# preOrderTraversal(newBt)
# print()
# inOrderTraversal(newBt)
# print()
# postOrderTraversal(newBt)
# print()

levelOrderTraversal(newBt)
print()
blackTea = TreeNode('black tea')
greenTea = TreeNode('green tea')
insert(newBt, blackTea)
insert(newBt, greenTea)

levelOrderTraversal(newBt)
print()
search(newBt, 'Fanta')




dpn = deepestNode(newBt)
print('deepestnode:->',dpn.data)
print()
# ans=deleteNode(newBt, dpn)
# print()
# print(ans)
# levelOrderTraversal(newBt)
# print()
delete(newBt, 'Tea')
# print()
levelOrderTraversal(newBt)
# print()
# deleteTree(newBt)
# print()
# levelOrderTraversal(newBt)