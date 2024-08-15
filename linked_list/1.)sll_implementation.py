class node :    # TO CREATE A NODE
    def __init__(self,key):
        self.key=key
        self.next=None

    def insertion_end(self, head, val):
        t = node(val)
        t1=head
        while t1.next != None:
            t1 = t1.next
        t1.next=t

    def deletion(self,head,n):
        t=head
        while n-2:
            t=t.next
            n-=1
        var=t.next
        t.next=t.next.next
        var.next = None

# def insertion(head,val):
#     t=node(val)
#     temp=head
#     while temp.next!=None:
#         temp=temp.next
#     temp.next=t


def printList(head):    # TO PRINT THAT LISNKED LIST
        t=head
        while t!=None :
            print(t.key,"",end='')
            t=t.next

head=node(16)
head.insertion_end(head,35)
head.insertion_end(head,46)
head.insertion_end(head,44)
head.insertion_end(head,52)
head.insertion_end(head,58)

printList(head)
head.deletion(head,4)
print()
printList(head)


# another implementation ||||^^^^||||
# head=node(10)
# head.next=node(20)
# head.next.next=node(30)
# printList(head)

