def rotate(matrix):
	
	x = len(matrix)

	"""
	for i in range(x//2 + x%2):
		for j in range(x//2):

			temp = matrix[i][j]
			matrix[i][j] = matrix[x-1-j][i] 
			matrix[x-1-j][i] = matrix[x-1-i][x-1-j]
			matrix[x-1-i][x-1-j] = matrix[j][x-1-i]
			matrix[j][x-1-i] = temp
	"""


	for i in range(x//2):
		for j in range(i, x-i-1):
			temp = matrix[i][j]
			print(temp)
			matrix[i][j] = matrix[x-1-j][i] 
			matrix[x-1-j][i] = matrix[x-1-i][x-1-j]
			matrix[x-1-i][x-1-j] = matrix[j][x-1-i]
			matrix[j][x-1-i] = temp


			#temp = matrix[j][i] # top left
			#matrix[j][i] = matrix[i][len(matrix)-1-j] # top left = bototm left
			#matrix[i][len(matrix)-1-j] = matrix[len(matrix)-1-j][len(matrix)-i-1] # bottom left = bottom right 
			#matrix[len(matrix)-1-j][len(matrix)-i-1] = matrix[len(matrix)-1-i][j]		# bottom right = top right
			


	print(matrix)



if __name__ == "__main__":
	rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]])

	x = ([[1,2,3,4,5],
		 [6,7,8,9,10],
		 [11,12,13,14,15],
		 [16,17,18,19,20],
		 [21,22,23,24,25]])
	rotate(x)