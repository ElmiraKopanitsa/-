# Данный файл создан Эльмирой Копаницей 03.01.2023 года по книге "Программируем на Пайтон" М.Доусона
# Задание: измените программу "Отгадай число" таким образом,
# чтобы у игрока было органиченное число попыток.
# Если игрок не укладывается в заданное число (и проигрывает),
# то программа должна выводить сколь возможно суровый текст.

import random
print("Добро пожаловать в игру 'Отгадай число'!")
print("\nЯ загадал натуральное число из диапазона от 1 до 100.")
print("Постарайтесь отгадать его за 10 попыток.\n")
# начальные значения
the_number = random.randint(1, 100)
guess = int(input("Ваше предположение: "))
tries = 1
# цикл отгадывания
while guess != the_number:
    if guess > the_number:
        print("Меньше..")
    else:
        print("Больше..")
    guess = int(input("Ваше предположение: "))
    tries += 1
    # предупреждение о последней попытке
    if tries == 9:
        print("Последняя попытка.")
    if tries == 10:
        break
# поздравление игрока
if guess != the_number:
    print("Отгадывание чисел явно не ваше дело.")
else:
    print("Вам удалось отгадать число! Это в самом деле", the_number)
    print("Вы затратили на отгадывание", tries, "попыток!\n")
input("\n\nНажмите Enter, чтобы выйти.")