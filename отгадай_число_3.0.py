# Данный файл создан Эльмирой Копаницей 03.01.2023 года по книге "Программируем на Пайтон" М.Доусона
# Напишите алгоритм игры, в которой случайное число от 1 до 100 загадывает человек,
# а отгадывает компьютер. Попробуйте реализовать алгоритм на Python
print("Загадайте число от 1 до 100, а я попробую его отгадать.")
input('Если вы загадали число, нажмите Enter.\nВведите "Ты угадал", если я угадал загаданное число.')
tries = 1
numbers = []
for i in range(1, 100+1):
    numbers.append(i)
number = numbers[len(numbers)//2]
print('Вы загадали число', number)
status = input('Загаданное число больше? Введите "да" или "нет"')
while status.lower() != "ты угадал":
    if status.lower() == "да":
        numbers = numbers[numbers.index(number):]
        number = numbers[len(numbers) // 2]
        print('Вы загадали число', number)
        status = input('Загаданное число больше? Введите "да" или "нет"')
        tries += 1
    else:
        numbers = numbers[:numbers.index(number)]
        number = numbers[len(numbers) // 2]
        print('Вы загадали число', number)
        status = input('Загаданное число больше? Введите "да" или "нет"')
        tries += 1

print("Круто! Я угадал ваше число всего за", tries, "попыток.")
input("\n\nНажмите Enter, чтобы выйти.")