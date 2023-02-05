# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16]
# [2, 3, 5, 6] => [12, 15]
list_1 = [7, 2, 4, 9, 5]
result = list ()
if len(list_1) % 2 != 0:
    for i in range(0, len(list_1) // 2 + 1 ):
        list_2 = list_1[i] * list_1[len(list_1) - i - 1]
        result += [list_2]
else:
    for i in range(0, len(list_1) // 2):
        list_2 = list_1[i] * list_1[len(list_1) - i - 1]
        result += [list_2]

print (result)

    

    

