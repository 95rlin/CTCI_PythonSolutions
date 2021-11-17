from linked_list import LinkedList
	
def partition(ll, val):
	print(val)


if __name__ == "__main__":
    ll = LinkedList.generate(10, 0, 9)
    print(ll)
    partition(ll, ll.head.value)
   
    