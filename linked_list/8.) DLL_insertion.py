class node :
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

def insert_begin(head,nodeToinsert):
    t=head
    v=nodeToinsert

    v.next=t  #putting referece of head node into the [next] of node which we want to insert
    t.prev=v  #putting reference of new node in a [prev] of the node to which the head is really linked
    t=v       #changing link of head to new node at beginning
    print("insert node at beginning-->  ",end=" ")
    return t

def insert_end(head,newNodeAtEnd):
    t=head
    v=newNodeAtEnd
    while t.next:
        t=t.next
    v.prev=t
    t.next=v
    print("insert node at ending-->  ", end=" ")

def insert_inbetween(head,newNodeinbetween,position):
    t=head
    v=newNodeinbetween
    pos=position
    while (pos-1):
        t=t.next
        pos-=1
    # newLink=t.next  (another approach --> just create new pointer linking to the node next to the node at which the t is pointing)
    v.prev=t
    t.next.prev=v
    v.next=t.next
    t.next=v
    print("insert node in_between--> ",end=" ")

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

# ============================= INSWERTION AT BEGINNING ============================
newNodeAtBeginning= node(5)
head =insert_begin(head,newNodeAtBeginning)
PrintList(head)

# ============================= INSWERTION AT ending ============================

newNodeAtEnding=node("hello")

insert_end(head,newNodeAtEnding)
PrintList(head)

# ============================= INSWERTION In Between  ============================

newNodeAtInbetween=node(100)
after_which_position=3
insert_inbetween(head,newNodeAtInbetween,after_which_position)
PrintList(head)




