from collections import Counter
import math


def sliding_window(string, test_set):
	left=0
	right=0 
	best_answer = math.inf
	c = Counter()
	for right, value in enumerate(string):
		c.update(value) 	# element to counter
		if done(c, test_set):
			while done(c, test_set):
				c.subtract(string[left])
				left+=1
			if (right - left + 2) < best_answer:
				best_answer = right - left + 2
	return best_answer

def done(cur_cnt, test_set):
	for letter in test_set:
		if cur_cnt[letter] == 0:
			return False
	return True # finished, all characters found

if __name__ == '__main__':
   test = ["a", "b", "c"]
   c = "dadddbbdca"

   sliding_window(c,test)
