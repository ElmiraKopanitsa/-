# Данный файл создан Эльмирой Копаницей 22.01.2023 года по книге "Программируем на Пайтон" М.Доусона
# Напишите программу, которая бы считала по просьбе пользователя.
# Надо позволить пользователю ввести начало и конец счета, а также интервал между называемыми целыми числами.
print(
    """
    Данная программа посчитает за вас.
    Вам нужно лишь ввести начало и конец отсчета, а также интервал счета 
    (например интервал 2, чтобы считать только каждое второе число).
    """
)
start = int(input("Введите начало счета: "))
finish = int(input("Введите конец счета: "))
step = int(input("Введите интервал счета: "))
for i in range(start, finish+1, step):
    print(i)
input("\n\nНажмите Enter, чтобы выйти.")
