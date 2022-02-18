pascal_triangle = []
size = 10

for i in range(size):
    row = [1] * (i + 1)
    for j in range(i + 1):
        if j != 0 and j != i:
            row[j] = pascal_triangle[i-1][j-1] + pascal_triangle[i-1][j]
    pascal_triangle.append(row)

for row in pascal_triangle:
    print(row)