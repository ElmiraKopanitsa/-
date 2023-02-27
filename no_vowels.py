# Данный файл создан Эльмирой Копаницей 21.01.2023 года по книге "Программируем на Пайтон" М.Доусона
# Только согласные
# Демонстрирует, как создавать новые строки из исходных с помощью цикла for
message = input("Введите текст: ")
new_message = ""
VOWELS = "aeiouаеёиоуыэюя"
print()
for letter in message:
    if letter.lower() not in VOWELS:
        new_message += letter
        print("Создана новая строка:", new_message)
print("\nВот ваш текст с изъятыми гласными буквами:", new_message)
input("\n\nНажмите Enter, чтобы выйти.")