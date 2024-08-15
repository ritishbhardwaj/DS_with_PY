class node:
    def __init__(self,key):
        self.key=key
        self.next=None
        self.prev=None


def PrintList(head):
    t=head
    while t:
        print(t.key,end=" ")
        t=t.next
    print()

def del_beg(head):
    t=head
    t=t.next
    return t

def reverse(head):
    t=head
    while t.next:
        t=t.next



head=node(10)
temp1=node(20)
temp2=node(30)
temp3=node(40)
head.next=temp1
temp1.prev=head
temp1.next=temp2
temp2.prev=temp1
temp2.next=temp3
temp3.prev=temp2


PrintList(head)

head=del_beg(head)
PrintList(head)

head=reverse(head)
PrintList(head)
