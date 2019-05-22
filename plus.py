import random
#m = 3
#n = 5
m = int(input('Введите целое m: '))
n = int(input('Введите целое n: '))
matrix = []
for i in range(1, m + 1):
	row = []
	for j in range(1, n + 1):
		row.append(random.randrange(2))
	matrix.append(row)
print('matrix:', matrix)

cells = []
for i in range(len(matrix)):
	for j in range(len(matrix[i])):
		if matrix[i][j] == 1:
				cells.append('(i' + str(i + 1) + ';j' + str(j + 1) + ')')
print('cells:', cells)