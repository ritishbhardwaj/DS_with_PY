class node:
    def __init__(self,key):
        self.key=key
        self.next=None
def search(head,x):
    t=head
    pos=1
    while t!=None:
        if t.key==x:
            print(t.key,"",pos)
            break
        elif t.key!=x :
            print("sorry we could'nt find the value in LL")
            break
        else:
            t=t.next
            pos+=1

    return -1


head=node(10)
head.next=node(20)
head.next.next=node(25)
head.next.next.next=node(30)
find=2
search(head,find)
