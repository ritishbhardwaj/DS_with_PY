class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=next

class LinkedList:
    def __init__(self):
        self.head=None
    def __iter__(self):
        curNode=self.head
        while curNode:
            yield curNode
            curNode=curNode.next

class Stack:
    def __init__(self):
        self.LinkedList=LinkedList()

    def __str__(self):
        if self.LinkedList:
            val=[str(x.value) for x in self.LinkedList]
            return '\n'.join(val)
        else:
            return 'not created or deleted recently'

    def isEmpty(self):
        if self.LinkedList.head==None:
            return True
        else:
            return False

    def push(self,val):
        node=Node(val)
        node.next=self.LinkedList.head
        self.LinkedList.head=node

    def pop(self):
        if self.isEmpty():
            return -1
        else:
            nodeValue=self.LinkedList.head.value
            self.LinkedList.head=self.LinkedList.head.next
            return nodeValue
    def peek(self):
        if self.isEmpty():
            return -1
        else:
            nodeValue=self.LinkedList.head.value
            return nodeValue
    def delete(self):
        self.LinkedList.head=None



customStack=Stack()
customStack.push(1)
customStack.push(2)
customStack.push(3)
print(customStack)
customStack.pop()
print()
print(customStack)
print()
peekVal=customStack.peek()
print(peekVal)
customStack.delete()
print(customStack)

