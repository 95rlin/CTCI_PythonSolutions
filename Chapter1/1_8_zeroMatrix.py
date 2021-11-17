def zero_matrix(x): # matrix is x
	row = set()
	col = set()

	for i in range(len(x)):
		for j in range(len(x[0])):
			if x[i][j] == 0:
				row.add(i)
				col.add(j)


	for i in set(row):
		for j in range(len(x[0])):
			x[i][j] = 0

	for i in set(col):
		for j in range(len(x)):
			x[j][i] = 0
			
	print(x)


if __name__ == "__main__":
	zero_matrix([[1,2,0],
				[4,5,6],
				[0,8,9]])

	zero_matrix([
                [1, 2, 3, 4, 0],
                [6, 0, 8, 9, 10],
                [11, 12, 13, 14, 15],
                [16, 0, 18, 19, 20],
                [21, 22, 23, 24, 25],
            ],)
