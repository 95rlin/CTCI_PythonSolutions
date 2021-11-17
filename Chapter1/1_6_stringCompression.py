from collections import Counter

def StringComp(arg):

	"""
	new_string = ""
	cnt = Counter(arg)
	for i in cnt:
		new_string = new_string + i + cnt[i]
	if len(new_string) >= len(arg):
		return arg
	else:
		return new_string
	"""
	new_string=""
	counter=1
	prev=arg[0]


	for i in range(1,len(arg)):
		print(arg[i], prev)		
		if arg[i] == prev:
			counter+=1
		elif arg[i] != prev:
			new_string+=prev+str(counter)
			prev = arg[i]
			counter=1
	new_string+=prev+str(counter)
	if len(new_string) >= len(arg):
		return arg
	else:
		return new_string





if __name__ == "__main__":
	print(StringComp("aabcccccaaa"))