# Данный файл создан Эльмирой Копаницей 21.01.2023 года по книге "Программируем на Пайтон" М.Доусона
# Случайные буквы
# Демонстрирует индексацию строк
import random
word = 'elmira'
print("\n\nВ переменной word хранится свово: ", word, "\n")
high = len(word)
low = -len(word)
for i in range(10):
    index = random.randrange(low, high)
    print(f"word[{index}]-", word[index])
input("\n\nНажмите Enter, чтобы выйти.")