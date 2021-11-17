def isSubstring(small,big):
	return (small in big)

def stringRotation(s1, s2):

	if s1 == s2:
		return True
	if len(s1) <= len(s2):
		small,big = s1,s2
	else:
		small,big = s2,s1

	left, right = 0,0

	while(right - left < len(small) and right < len(big)):
		if big[right] == small[left] and left==0:
			left=right
		elif big[right] != small[right-left]:
			left=0
		right+=1	

	if left == 0:
		return False
	else:
		return isSubstring(small, big[left:]+big[0:left])

def string_rotation(s1, s2): # smart ass solution only works when both strings s1 and s2 are the same size
    if len(s1) == len(s2) != 0:
        return s2 in s1 * 2
    return False


if __name__ == "__main__":
	#print(stringRotation("waterbottle", "erbottlewat"))
	#print(stringRotation("waterbottle", "bottle"))
	#print(stringRotation("waterbottle", "ewaterbottl"))
	#print(stringRotation("waterbottle", "waterbttle"))
	print(string_rotation("waterbottle", "erbottlewat"))
	print(string_rotation("bottle", "waterbottle"))

