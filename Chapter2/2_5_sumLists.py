from linked_list import LinkedList
from linked_list import LinkedListNode



def addTwoNumbers(l1, l2): # First Attempt (messy and slow)
    temphead = LinkedListNode(0)
    current = temphead
    while(l1 or l2):
        if not current.next:
            current.next = LinkedListNode(0)
        current = current.next
        l1val=0 if not l1 else l1.value
        l2val=0 if not l2 else l2.value
        sum_val = l1val + l2val
        #print(sum_val)
        if current.value + sum_val > 9:
            current.value = (current.value + sum_val)%10
            current.next = LinkedListNode(1)
            #current = current.next
        else:
            current.value = current.value + sum_val
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
    return temphead.next

def addTwoNumbers(l1,l2):
    carry = 0
    temphead = current = LinkedListNode(0)
    while(l1 or l2 or carry):
        if l1:
            carry+=l1.value
            l1=l1.next
        if l2:
            carry+=l2.value
            l2=l2.next
        carry,val = divmod(carry,10)
        current.next = current = LinkedListNode(val)
    return temphead.next

if __name__ == "__main__":

    l1 = LinkedList.generate(4, 0, 9)
    l2 = LinkedList.generate(4, 0, 9)
    print(l1)
    print(l2)

    new = addTwoNumbers(l1.head,l2.head)

    while(new):
        print(str(new.value) + " -> ", end='')
        new = new.next