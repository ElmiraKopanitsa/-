# Данный файл создан Эльмирой Копаницей 03.01.2023 года по книге "Программируем на Пайтон" М.Доусона
# Демонстирует условную интерпретацию значений
print("Добро пожаловать в Шато-де-Перекуси!")
print("Кажется, нынешним вечером у нас все столики заняты.\n")
money = int(input("Сколько долларов вы готовы дать метрдотелю на чай? "))
if money:
    print("Прошу прощения, мне сообщили, что есть один свободный столик. Сюда, пожалуйста.")
else:
    print("Присаживайтесь, будьте добры. Придется подождать.")
input("\n\nНажмите Enter, чтобы выйти.")