import time
import unittest

def one_away(arg1, arg2):
	#print(arg1, arg2)
	"""
	counter = 0
	if len(arg1) >= len(arg2):
		big = list(arg1)
		small = list(arg2)

	for i in range(len(big)):
		if big[i] != small[i] 
	"""


	if len(arg1) == len(arg2):
		return replace_check(arg1,arg2)
	elif len(arg1) + 1 == len(arg2):
		return insert_check(arg1,arg2)
	elif len(arg1) - 1 == len(arg2):
		return insert_check(arg2,arg1)
	else:
		return False


def replace_check(arg1,arg2):
	counter = 0
	for i in range(len(arg1)):
		if arg1[i] != arg2[i]:
			counter+=1
		if counter > 1:
			return False
	return True 


"""
def insert_check(small, large):
	combine = small + large
	return len(set(combine)) <= len(small) + 1 # this doesnt work, because order DOES matter
'"""

"""
def insert_check(small, large):
	counter = 0
	for i in range(len(small)) :
		if small[i - counter] != large[i]:
			counter+=1
		if counter > 1:
			return False
	return True 
"""


def insert_check(small, big):
	i,j = 0,0
	while i<len(small) and j<len(big):
		if small[i] != big[j]:
			j+=1
			if (j - i) >= 2:
				return False
		else:
			i+=1
			j+=1
	return True

class Test(unittest.TestCase):
    test_cases = [
        # no changes
        ("pale", "pale", True),
        ("", "", True),
        # one insert
        ("pale", "ple", True),


        ("ple", "pale", True),
        ("pales", "pale", True),

        ("ples", "pales", True),
        ("pale", "pkle", True),
        ("paleabc", "pleabc", True),
        ("", "d", True),
        ("d", "de", True),
        # one replace
        ("pale", "bale", True),
        ("a", "b", True),
        ("pale", "ble", False),
        # multiple replace
        ("pale", "bake", False),
        # insert and replace
        ("pale", "pse", False),
        ("pale", "pas", False),
        ("pas", "pale", False),
        ("pkle", "pable", False),
        ("pal", "palks", False),
        ("palks", "pal", False),
        # permutation with insert shouldn't match
        ("ale", "elas", False),
    ]


    testable_functions = [one_away]
    def test_one_away(self):

        for f in self.testable_functions:
            start = time.perf_counter()
            for _ in range(100):
                for [text_a, text_b, expected] in self.test_cases:
                    assert f(text_a, text_b) == expected

            duration = time.perf_counter() - start
            print(f"{f.__name__} {duration * 1000:.1f}ms")


if __name__ == "__main__":
    unittest.main()

    #print(one_away("ale", "elas"))

    #print(one_away("pales", "pale"))

