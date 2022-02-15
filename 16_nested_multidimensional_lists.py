line = [1, 7, 6, 11, 3]
# создание двумерного списка
image = [line[:] for _ in range(len(line))]
print(image)
# lst[index][index] - выбор элемента в двумерном списке
print(image[0][1])
# заменя рядка
image[1] = [0] * len(line)
print(image)
# замена с помощью срезов
image[1][:] = [1] * len(line)
print(image)