tuples = [(i, j)
          for i in range(1, 7) if i % 3 == 0
          for j in range(1, 11) if j % 2 == 0 and j % 3 == 0
          ]
print(tuples)

tuples_mult = [f'{i} * {j} = {i * j}'
               for i in range(1, 11)
               for j in range(11, 21)
               ]

print(tuples_mult)

m, n = 3, 4

matrix = [[number for number in range(m)] for _ in range(n)]
print(matrix)

excludes_numbers = [4, 0]

square_matrix = [(number + 1) ** 2
                 for row in matrix
                 for number in row
                 if number not in excludes_numbers
                 ]
print(square_matrix)

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
# транспонирование матрицы
trans_matrix = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(trans_matrix)
