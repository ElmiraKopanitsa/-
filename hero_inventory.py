# Данный файл создан Эльмирой Копаницей 22.01.2023 года по книге "Программируем на Пайтон" М.Доусона
# Арсенал героя
# Демонстрирует создание кортежа
# создадим пустой кортеж
inventory = ()
# рассмотрим его как условие
if not inventory:
    print("Вы безоружны.")
input("\nНажмите Enter, чтобы продолжить.")
# теперь создадит кортеж с несколькими элементами
inventory = ("меч", "кольчуга", "щит", "целебное снадобье")
# выведем этот кортеж на экран
print("\nСодержимое кортежа: ")
print(inventory)
# выведем все элементы последовательно
print("\nИтак, в вашем арсенале:")
for item in inventory:
    print(item)
input("\n\nНажмите Enter, чтобы выйти.")