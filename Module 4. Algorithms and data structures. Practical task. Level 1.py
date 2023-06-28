# бинарный поиск
def binary_search(mass, element):
    left = 0
    right = len(mass) - 1

    while left <= right:
        center = (left + right) // 2
        if element == mass[center]:
            print(f"Индекс искомого элемента: {center}")
            break
        if element > mass[center]:
            left = center + 1
        else:
            right = center - 1
    else:
        print("Искомое значение отсутствует")


mass = [1, 2, 3, 4, 5, 6, 7, 8, 9]

binary_search(mass, 3)
binary_search(mass, 33)
