class node:
    def __init__(self,key):
        self.key=key
        self.next=None


def printList(head):
    t=head
    while t:
        print(t.key,end=" ")
        t=t.next
    return ""

def reverse_iteration(head):
    curr=prev=nextnode=head
    prev=nextnode=None

    while curr:
        nextnode=curr.next
        curr.next=prev
        prev=curr
        curr=nextnode
    return prev   #prev will be our new head

head=node(10)
head.next=node(20)
head.next.next=node(25)
head.next.next.next=node(30)
fifthNode=head.next.next.next.next=node(40)
fifthNode.next=node(50)
fifthNode.next.next=node(60)

print(printList(head),"  <-- These are the elements of linked list")

head=reverse_iteration(head)
print(printList(head),"  <-- This is reverse linked list")


