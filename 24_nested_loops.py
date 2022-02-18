for i in range(1, 6):
    print(f'{i} : (', end='')
    for j in range(1, 6):
        print(f'{j}', end=' ')
    print(')')

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for row in matrix:
    for item in row:
        print(item, type(item),end=' ')
    print()

matrix1 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
matrix2 = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]]
matrix_union = []

for i in range(len(matrix1)):
    for j in range(len(matrix1[i])):
        matrix_union.append(matrix1[i][j] + matrix2[i][j])

print(matrix_union)
matrix_union.clear()

for index, row in enumerate(matrix1):
    for index_inner, value in enumerate(matrix1[index]):
        matrix_union.append(value + matrix2[index][index_inner])

print(matrix_union)

text = [
    'First  line 1',
    'Second       line         2',
    'Third    line   3'
]

for index, line in enumerate(text):
    while '  ' in line:
        line = line.replace('  ', ' ')
        print(line)
    text[index] = line

print(text)

# транспонирование матрицы
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

for i in range(len(matrix)):
    for j in range(i+1, len(matrix)):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

for row in matrix:
    for item in row:
        print(item, end='\t')
    print()
