import math
from collections import Counter



def pal_perm_pythonic(arg):
	arg = arg.replace(" ", "")
	return len(set(arg)) == math.ceil(len(arg)/2)

def pal_perm_collections(arg):
	arg = Counter(arg.replace(" ", ""))
	return sum(val%2 for val in arg.values()) <= 1




if __name__ == "__main__":
	print(pal_perm_pythonic("racecar"))
	print(pal_perm_collections("racecar"))