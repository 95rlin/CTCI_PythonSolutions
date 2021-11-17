
def URLify(arg):
	for i in range(len(arg)):
		arg = list(arg)
		if arg[i] == " ":
			arg[i] = "%20"
	s = ""
	return s.join(arg)

	#runtime = O(n)

def URLify_2(text, length):
    """solution using standard library"""
    return text[:length].replace(" ", "%20")

if __name__ == "__main__":
	test = "Hello how are you     "
	print(URLify("Hello I am a potatoe"))
	print(URLify_2(test, len(test)))