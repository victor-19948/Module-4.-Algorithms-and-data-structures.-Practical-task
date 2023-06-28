# сортировка вставками
def insertion_sort(mass):
    n = len(mass)
    for i in range(1, n):
        for j in range(i, 0, -1):
            if mass[j] < mass[j - 1]:
                mass[j], mass[j - 1] = mass[j - 1], mass[j]
            else:
                break


mass = [1, 9, 2, 8, 3, 7, 4, 6, 5]

print(mass)
insertion_sort(mass)
print(mass)
