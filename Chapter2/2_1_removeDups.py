from linked_list import LinkedList
	
def remove_dups(ll):
	if ll.head is None:
		return
	previous = None
	current = ll.head
	seen = set([ll.head])
	while(current):
		if current.value in seen:
			previous.next = current.next
		else:
			previous = current
			seen.add(current.value)
		current = current.next
	ll.tail = previous
	return ll


if __name__ == "__main__":
    ll = LinkedList.generate(10, 0, 9)
    print(ll)
    remove_dups(ll)
    print(ll)