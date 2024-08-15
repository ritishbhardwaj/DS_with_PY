class node:
    def __init__(self,key):
        self.key=key
        self.next=None

def printList(head):
    t=head
    while t:
        print(t.key, "", end="")
        t = t.next

def del_beg(head):
    t=head
    t=t.next
    return t

def del_end(head):
    t=head
    while t.next.next!=None:
        t=t.next
    print("--",t.key,"--")
    t.next=None
    return

def del_inbetween(head,position):
    t=head
    loc=position
    while loc-2:
        loc-=1
        t=t.next
    t.next=t.next.next
    return

head=node(10)
head.next=node(20)
head.next.next=node(25)
head.next.next.next=node(30)
head.next.next.next.next=node(40)
printList(head)
print("")
'''del from beginning'''
head=del_beg(head)
# printList(head)

'''del from end'''
del_end(head)
printList(head)

'''del in between '''
position=3
del_inbetween(head,position)
printList(head)