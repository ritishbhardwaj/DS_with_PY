'''

GLITCH IN RECURSIVE CALL
I DONNO WHY

'''



class node :
    def __init__(delf,key):
        delf.key=key
        delf.next=None

def print_List(head):
        t=head
        while t:
            print(t.key,end=" ")
            t=t.next

def reversing_recursion(prev,t):

    if t:
        reversing_recursion(t,t.next)
        t.next=prev
        print(t.key)
    if (not t) :
        head=prev
        print(head.key)


head=node(10)
head.next=node(20)
head.next.next=node(25)
head.next.next.next=node(30)
fifthNode=head.next.next.next.next=node(40)
fifthNode.next=node(50)
fifthNode.next.next=node(60)

print_List(head)
print()
reversing_recursion(None,head)
print(head)
print_List(head)