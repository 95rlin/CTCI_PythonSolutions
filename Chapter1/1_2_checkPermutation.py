from collections import Counter

def check_permutation(s1,s2):
	return Counter(s1) == Counter(s2)

	# Create counter hash map for s1 and s2 and check if equal
	# runtime = 2n = O(n)




if __name__ == "__main__":
	print(check_permutation("abcd", "cbda"))
	print(check_permutation("abcdefghijk", "jkighfedcab"))