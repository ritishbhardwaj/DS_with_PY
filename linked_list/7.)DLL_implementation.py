class node:
    def __init__(self,key):
        self.key=key
        self.next=None
        self.prev=None

def Print(head):
    t=head
    while t:
        print(t.key,end=" ")
        t=t.next


head=node(5)
temp1=node(10)
temp2=node(20)
temp3=node(30)
head.next=temp1
temp1.prev=head
temp1.next=temp2
temp2.prev=temp1
temp2.next=temp3
temp3.prev=temp2


Print(head)
