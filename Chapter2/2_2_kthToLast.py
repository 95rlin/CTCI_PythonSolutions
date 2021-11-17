from linked_list import LinkedList
	
def return_kth_to_last(ll, k):
	L=R=ll.head
	for i in range(k-1):
		R = R.next
	while(R.next):
		R = R.next
		L = L.next
	return L.value	

def remove(ll, k):
	dummy=LinkedList.generate(0,0,0)
	dummy.next = ll.head
	L = R = dummy
	#L=R=ll.head
	for i in range(k):
		R = R.next
	while(R.next):
		R = R.next
		L = L.next
	L.next = L.next.next
	return ll
if __name__ == "__main__":
    ll = LinkedList.generate(1, 0, 9)
    print(ll)
    print(return_kth_to_last(ll, 1))
    print(remove(ll, 1))

    """
    ll = LinkedList.generate(10, 0, 9)
    print(ll)
    print(return_kth_to_last(ll, 1))
    print(remove(ll, 1))
    """