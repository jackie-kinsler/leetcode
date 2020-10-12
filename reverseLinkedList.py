class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __repr__(self):
        return f"<ListNode val:{self.val}>"

def reverseList(head):
    
    if head.next == None:
        return 
    
    prev = None
    current = head
    while current != None: 
        next = current.next
        current.next = prev
        prev = current
        current = next


def printList(head):
    node_list = []
    current = head

    while current != None: 
        node_list.append(current.val)
        current = current.next 
    print(node_list)




a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)

a.next = b
b.next = c
c.next = d
d.next = e

printList(a)
reverseList(a)
printList(e)

# print([a.val, b.val, c.val, d.val, e.val])

# reverseList(a)

# print([a.val, b.val, c.val, d.val, e.val])

