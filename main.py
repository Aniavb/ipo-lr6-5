"""
Написать программу, которая:
- Создаёт с помощью генератора списков, список случайных целых чисел от **-50** до **50** размером **25** элементов.
- Находит количество положительных, отрицательных и нулевых элементов в списке.
- Выводит значения и их (*положительных, отрицательных и нулевых*) количество вместе с процентом от общего количества.
- Выводит самое большое и самое маленькое значение
"""
import random  #подключаем модуль
a = [ random.randint(-50,50) for i in range(25)]   #с помощью генератора списков генерируем список случайных целых чисел
print(a)   #выводим список
print("Минимальное значение: ", min(a))   #выводим минимальное значение
print("Максимальное значение: ", max(a))   #выводим максимальное
count_positive = 0   #счётчик для положительных чисел
count_negative = 0   #счётчик для отрицательных чисел
count_zero = 0   #для нулевых
for i in a:   #перебираем элементы в списке
    if i>0:   #если элемент > 0
        count_positive += 1   #увеличиваем счётчик на 1
        percent1 = count_positive/25 * 100   #находим процент от общего количества
    if i<0:
        count_negative +=1
        percent2 = count_negative/25 * 100
    if i%10 == 0:
        count_zero +=1
        percent3 = count_zero/25 * 100   #
print(f"Количество положительных чисел: {count_positive}, и их процент от общего количества: {percent1}")   #выводим
print(f"Количество отрицательных чисел: {count_negative}, и их процент от общего количества: {percent2}")
print(f"Количество нулевых чисел: {count_zero}, и их процент от общего количества: {percent3}")