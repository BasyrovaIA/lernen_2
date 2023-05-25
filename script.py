#17/9 задание
number = input('Введите последовательность чисел через пробел от 0 до 100: ')

array = list(map(int, number.split()))
print(array)

for i in range(len(array)):
    for j in range(len(array) - i - 1):
        if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]
print(array)

def binary_search(array, element, left, right):
    if left > right:  # если левая граница превысила правую,
        return print('такого числа нет в массиве')  # значит элемент отсутствует
    middle = (right + left) // 2  # находимо середину
    if array[middle] == element:  # если элемент в середине,
        return middle  # возвращаем этот индекс
    elif element < array[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(array, element, left, middle - 1)
    else:  # иначе в правой
        return binary_search(array, element, middle + 1, right)

element = int(input('Введите одно число: '))

print(binary_search(array, element, 0, len(array)-1))
# запускаем алгоритм на левой и правой границе

