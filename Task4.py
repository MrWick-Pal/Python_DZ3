# Напишите программу, которая будет преобразовывать 
# десятичное число в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10
string = ''
number = int(input('Введите число: '))
while number != 0:
    string += str(number % 2) 
    number //= 2
print(string)