
# print(maxs, count)
# Вам дан словарь per_cent с распределением процентных ставок по вкладам в различных банках таким образом,
# что ключ — название банка, значение — процент. Напишите программу, в результате которой будет сформирован
# список deposit значений — накопленные средства за год вклада в каждом из банков.
# На вход программы с клавиатуры вводится сумма money, которую человек планирует положить под проценты.


# money = float(input("введите сумму для накопелений "))
# per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
# nacop = list(map(float, per_cent.values()))
# print(nacop)
# i=1
# for i in nacop:
#     deposit = [money * i / 100]
#     print(deposit)

# import math
# n = 10000
# print(n ** 2 / (n * math.log(n, 2)))

# N_max = int(input("Определите размер очереди:"))
#
# queue = [0 for _ in range(N_max)]  # инициализируем список с нулевыми элементами
# order = 0  # будем хранить сквозной номер задачи
# head = 0  # указатель на начало очереди
# tail = 0  # указатель на элемент следующий за концом очереди
#
#
#
# def is_empty(): # очередь пуста?
#     # да, если указатели совпадают и в них содержится ноль
#     return head == tail and queue[head] == 0
#
# def size(): # получаем размер очереди
#     if is_empty(): # если она пуста
#         return 0 # возвращаем ноль
#     elif head == tail: # иначе, если очередь не пуста, но указатели совпадают
#         return N_max # значит очередь заполнена
#     elif head > tail: # если хвост очереди сместился в начало списка
#         return N_max - head + tail
#     else: # или если хвост стоит правее начала
#         return tail - head
#
#
# def add():  # добавляем задачу в очередь
#     global tail, order
#     order += 1  # увеличиваем порядковый номер задачи
#     queue[tail] = order  # добавляем его в очередь
#     print("Задача №%d добавлена" % (queue[tail]))
#
#     # увеличиваем указатель на 1 по модулю максимального числа элементов
#     # для зацикливания очереди в списке
#     tail = (tail + 1) % N_max
# def show(): # выводим приоритетную задачу
#     print("Задача №%d в приоритете" % (queue[head]))
#
# def do(): # выполняем приоритетную задачу
#     global head
#     print("Задача №%d выполнена" % (queue[head]))
#     queue[head] = 0 # после выполнения зануляем элемент по указателю
#     head = (head + 1) % N_max # и циклично перемещаем указатель
#
# while True:
#     cmd = input("Введите команду:")
#     if cmd == "empty":
#         if is_empty():
#             print("Очередь пустая")
#         else:
#             print("В очереди есть задачи")
#     elif cmd == "size":
#         print("Количество задач в очереди:", size())
#     elif cmd == "add":
#         if size() != N_max:
#             add()
#         else:
#             print("Очередь переполнена")
#     elif cmd == "show":
#         if is_empty():
#             print("Очередь пустая")
#         else:
#             show()
#     elif cmd == "do":
#         if is_empty():
#             print("Очередь пустая")
#         else:
#             do()
#     elif cmd == "exit":
#         for _ in range(size()):
#             do()
#         print("Очередь пустая. Завершение работы")
#         break
#     else:
#         print("Введена неверная команда")

#
# G = {"Адмиралтейская" :
#          {"Садовая" : 4},
#      "Садовая" :
#          {"Сенная площадь" : 3,
#           "Спасская" : 3,
#           "Адмиралтейская" : 4,
#           "Звенигородская" : 5},
#      "Сенная площадь" :
#          {"Садовая" : 3,
#           "Спасская" : 3},
#      "Спасская" :
#          {"Садовая" : 3,
#           "Сенная площадь" : 3,
#           "Достоевская" : 4},
#      "Звенигородская" :
#          {"Пушкинская" : 3,
#           "Садовая" : 5},
#      "Пушкинская" :
#          {"Звенигородская" : 3,
#           "Владимирская" : 4},
#      "Владимирская" :
#          {"Достоевская" : 3,
#           "Пушкинская" : 4},
#      "Достоевская" :
#          {"Владимирская" : 3,
#           "Спасская" : 4}}
#
# D = {k : 100 for k in G.keys()} # расстояния
# start_k = 'Адмиралтейская' # стартовая вершина
# D[start_k] = 0 # расстояние от нее до самой себя равно нулю
# U = {k : False for k in G.keys()} # флаги просмотра вершин
# P = {k : None for k in G.keys()} # предки
#
# for _ in range(len(D)):
#     # выбираем среди непросмотренных наименьшее по расстоянию
#     min_k = min([k for k in U.keys() if not U[k]], key = lambda x: D[x])
#
#     for v in G[min_k].keys(): # проходимся по всем смежным вершинам
#          if D[v] > D[min_k] + G[min_k][v]: # если расстояние от текущей вершины меньше
#             D[v] = D[min_k] + G[min_k][v] # то фиксируем его
#             P[v] = min_k # и записываем как предок
#     U[min_k] = True # просмотренную вершину помечаем
# some_station = 'Владимирская'
# pointer = some_station # куда должны прийти
# while pointer is not None: # перемещаемся, пока не придём в стартовую точку
#     print(pointer)
#     pointer = P[pointer]

# class BinaryTree:
#     def __init__(self, value):
#         self.value = value
#         self.left_child = None
#         self.right_child = None
#
#     def insert_left(self, next_value):
#         if self.left_child is None:
#             self.left_child = BinaryTree(next_value)
#         else:
#             new_child = BinaryTree(next_value)
#             new_child.left_child = self.left_child
#             self.left_child = new_child
#         return self
#
#     def insert_right(self, next_value):
#         if self.right_child is None:
#             self.right_child = BinaryTree(next_value)
#         else:
#             new_child = BinaryTree(next_value)
#             new_child.right_child = self.right_child
#             self.right_child = new_child
#         return self
#
#     def pre_order(self):
#      print(self.value) # процедура обработки
#
#      if self.left_child is not None: # если левый потомок существует
#         self.left_child.pre_order() # рекурсивно вызываем функцию
#
#      if self.right_child is not None: # если правый потомок существует
#         self.right_child.pre_order() # рекурсивно вызываем функцию
#
#     def post_order(self):
#      if self.left_child is not None: # если левый потомок существует
#         self.left_child.post_order() # рекурсивно вызываем функцию
#
#      if self.right_child is not None: # если правый потомок существует
#         self.right_child.post_order() # рекурсивно вызываем функцию
#
#      print(self.value) # процедура обработки
#
# # создаём корень и его потомков /7|2|5\
# node_root = BinaryTree(2).insert_left(7).insert_right(5)
# # левое поддерево корня /2|7|6\
# node_7 = node_root.left_child.insert_left(2).insert_right(6)
# # правое поддерево предыдущего узла /5|6|11\
# node_6 = node_7.right_child.insert_left(5).insert_right(11)
# # правое поддерево корня /|5|9\
# node_5 = node_root.right_child.insert_right(9)
# # левое поддерево предыдущего узла корня /4|9|\
# node_9 = node_5.right_child.insert_left(4)
#
# node_root.post_order()
#
#
# def in_order(self):
#     if self.left_child is not None: # если левый потомок существует
#         self.left_child.in_order() # рекурсивно вызываем функцию
#
#     print(self.value) # процедура обработки
#
#     if self.right_child is not None: # если правый потомок существует
#         self.right_child.in_order() # рекурсивно вызываем функцию

#
# class Node:  # класс элемента
#     def __init__(self, value=None, next_=None):  # инициализируем
#         self.value = value  # значением
#         self.next = next_  # и ссылкой на следующий элемент
#
#     def __str__(self):
#         return "Node value = " + str(self.value)
#
#
# class LinkedList:  # класс списка
#     def __init__(self):  # инициализируем пустым
#         self.first = None
#         self.last = None
#
#     def clear(self):  # очищаем список
#         self.__init__()
#
#     def __str__(self):  # функция печати
#         R = ''
#
#         pointer = self.first  # берем первый указатель
#         while pointer is not None:  # пока указатель не станет None
#             R += str(pointer.value)  # добавляем значение в строку
#             pointer = pointer.next  # идем дальше по указателю
#             if pointer is not None:  # если он существует добавляем пробел
#                 R += ' '
#         return R
#
#     def pushleft(self, value):
#         if self.first is None:
#             self.first = Node(value)
#             self.last = self.first
#         else:
#             new_node = Node(value, self.first)
#             self.first = new_node
#
#
#     def pushright(self, value):
#         if self.first is None:
#              self.first = Node(value)
#              self.last = self.first
#         else:
#             new_node = Node(value)
#             self.last.next = new_node
#             self.last = new_node
#     def popleft(self):
#         if self.first is None: # если список пустой, возвращаем None
#             return None
#         elif self.first == self.last: # если список содержит только один элемент
#             node = self.first # сохраняем его
#             self.__init__() # очищаем
#             return node # и возвращаем сохраненный элемент
#         else:
#             node = self.first # сохраняем первый элемент
#             self.first = self.first.next # меняем указатель на первый элемент
#             return node # возвращаем сохраненный\
#
#     def popright(self):
#         if self.first is None: # если список пустой, возвращаем None
#             return None
#         elif self.first == self.last: # если список содержит только один элемент
#             node = self.first # сохраняем его
#             self.__init__() # очищаем
#             return node # и возвращаем сохраненный элемент
#         else:
#             node = self.last # сохраняем последний
#             pointer = self.first # создаем указатель
#             while pointer.next is not node: # пока не найдем предпоследний
#                 pointer = pointer.next
#             pointer.next = None # обнуляем указатели, чтобы
#             self.last = pointer # предпоследний стал последним
#             return node # возвращаем сохраненный
#
# # LL = LinkedList()
# #
# # LL.pushright(1)
# # LL.pushleft(2)
# # LL.pushright(3)
# # LL.popright()
# # LL.pushleft(4)
# # LL.pushright(5)
# # LL.popleft()
# #
# # print(LL)
#
#     def __iter__(self): # объявляем класс как итератор
#         self.current = self.first # в текущий элемент помещаем первый
#         return self # возвращаем итератор
#
#     def __next__(self): # метод перехода
#         if self.current is None: # если текущий стал последним
#             raise StopIteration # вызываем исключение
#         else:
#             node = self.current # сохраняем текущий элемент
#             self.current = self.current.next # совершаем переход
#             return node # и возвращаем сохраненн
#
#     def __len__(self):
#         count = 0
#         pointer = self.first
#         while pointer is not None:
#             count += 1
#             pointer = pointer.next
#         return count
#
#
# LL = LinkedList()
#
# LL.pushright(1)
# LL.pushleft(2)
# LL.pushright(3)
# LL.popright()
# LL.pushleft(4)
# LL.pushright(5)
# LL.popleft()
#
# print(LL)

# #Линейный поиск
# def find(array, element):
#     for i, a in enumerate(array):
#         if a == element:
#             return i
#     return False
#
# array = list(map(int, input().split()))
# element = int(input())
#
# print(find(array, element))
#
# #Напишите функцию count, которая возвращает количество вхождений элемента в массив
#
# def count(array, element):
#     count = 0
#     for a in array:
#         if a == element:
#             count += 1
#     return count
#
#
# #Двоичный поиск
#
# def binary_search(array, element, left, right):
#     if left > right:  # если левая граница превысила правую,
#         return False  # значит элемент отсутствует
#
#     middle = (right + left) // 2  # находимо середину
#     if array[middle] == element:  # если элемент в середине,
#         return middle  # возвращаем этот индекс
#     elif element < array[middle]:  # если элемент меньше элемента в середине
#         # рекурсивно ищем в левой половине
#         return binary_search(array, element, left, middle - 1)
#     else:  # иначе в правой
#         return binary_search(array, element, middle + 1, right)
#
#
# element = int(input())
# array = [i for i in range(1, 100)]  # 1,2,3,4,...
#
# # запускаем алгоритм на левой и правой границе
# print(binary_search(array, element, 0, 99))

#array = [2, 3, 1, 4, 6, 5, 9, 8, 7]

# for i in range(len(array)):  # проходим по всему массиву
#     idx_min = i  # сохраняем индекс предположительно минимального элемента
#     for j in range(i, len(array)):
#         if array[j] < array[idx_min]:
#             idx_min = j
#
#     if i != idx_min:  # если индекс не совпадает с минимальным, меняем
#         array[i], array[idx_min] = array[idx_min], array[i]
#         print(i)
#
# print(array)
# print(j)
# count = 0
# #алгоритм сортировки вставками.
# for i in range(1, len(array)):
#     x = array[i]
#     idx = i
#     while idx > 0 and array[idx-1] > x:
#         cou += 1
#         array[idx] = array[idx-1]
#         idx -= 1
#     array[idx] = x
#
# print(array)
# print('сравнений: ', cou)

#алгоритм сортировки слиянием.
# def merge_sort(L):  # "разделяй"
#     if len(L) < 2:  # если кусок массива меньше 2,
#         return L[:]  # выходим из рекурсии
#     else:
#         middle = len(L) // 2  # ищем середину
#         left = merge_sort(L[:middle])  # рекурсивно делим левую часть
#         right = merge_sort(L[middle:])  # и правую
#         return merge(left, right)  # выполняем слияние
#
#
# def merge(left, right):  # "властвуй"
#     result = []  # результирующий массив
#     i, j = 0, 0  # указатели на элементы
#
#     # пока указатели не вышли за границы
#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#
#     # добавляем хвосты
#     while i < len(left):
#         result.append(left[i])
#         i += 1
#
#     while j < len(right):
#         result.append(right[j])
#         j += 1
#
#     return result



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

