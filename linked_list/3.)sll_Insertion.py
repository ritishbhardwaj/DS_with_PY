class node:
    def __init__(self,key):
        self.key=key
        self.next=None
def printList(head):
    t=head
    while t:
        print(t.key,"",end="")
        t=t.next

def Insertion_beg(head,nodeToInsert):
    v=nodeToInsert
    t=head
    v.next=t
    t=v
    return t

def Insertion_end(head,nodeToInsert):
    v=nodeToInsert
    t=head
    while t.next!=None:
        t=t.next
    t.next=v
    v.next=None
    return

def Insertion_inbetween(head,after_which,nodeToInsert):
        p=after_which
        v=nodeToInsert
        t=head
        for i in range(p-1):
            t=t.next
        v.next=t.next
        t.next=v
        return


head=node(10)
head.next=node(20)
head.next.next=node(25)
head.next.next.next=node(30)
newTobeg=node(5)
newToend=node(35)

'''insertion at beginning'''
head= Insertion_beg(head,newTobeg)
# printList(head)

'''insertion at end'''
Insertion_end(head,newToend)
# printList(head)

'''insertion in between the ll'''
value=node(27)
pos=4
Insertion_inbetween(head,pos,value)
printList(head)
print()