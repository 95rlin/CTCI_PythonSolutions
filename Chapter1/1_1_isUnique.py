from collections import Counter


def isUnique(arg):
	# input = abcdeeee
	# result = false 
	cnt = Counter(arg)
	for i in cnt.values():
		if i > 1:
			return False 
	return True 

	# Runtime = n + n == O(n)
def isUnique2(arg):
	return len(set(arg)) == len(arg)

	# Runtime = O(n)

if __name__ == '__main__':
	print(isUnique("abcde"))
	print(isUnique2("abcde"))
	