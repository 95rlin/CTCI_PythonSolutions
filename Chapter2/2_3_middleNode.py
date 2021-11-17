from linked_list import LinkedList
	
def deleteMiddleNode(mid):
	mid.value = mid.next.value
	mid.next = mid.next.next
	return mid


if __name__ == "__main__":
    ll = LinkedList.generate(10, 0, 9)
    node = ll.head.next.next.next.next
    print(ll)
    print(node)
    deleteMiddleNode(node)
    print(ll)
   
    