from linked_list import LinkedList
from linked_list import LinkedListNode
def partition(head, val):
        ltail = lhead = LinkedListNode(0)
        rtail = rhead = LinkedListNode(0)
        
        while(head):
            if head.value < val:
                ltail.next = head
                ltail = ltail.next
            else:
                rtail.next = head
                rtail = rtail.next
            head = head.next
            
        ltail.next = rhead.next
        rtail.next = None
        return lhead.next
        


if __name__ == "__main__":
    ll = LinkedList.generate(10, 0, 9)
    print(ll)
    new = partition(ll.head, ll.head.value)

    while(new):
    	print(str(new.value) + " -> ", end='')
    	new = new.next