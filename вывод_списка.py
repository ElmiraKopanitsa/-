# Данный файл создан Эльмирой Копаницей 25.01.2023 года по книге "Программируем на Пайтон" М.Доусона
# Создайте программу, которая будет выводить список в случайном порядке.
# На экране должны печататься без повторения все слова из представленного списка.
import random
my_list = ["book", "netbook", "laptop", "pen", "bookstick", "phone"]
while my_list:
    letter = random.randrange(len(my_list))
    print(my_list[letter])
    my_list = my_list[:letter] + my_list[letter + 1:]
input("\n\nНажмите Enter, чтобы выйти.")
