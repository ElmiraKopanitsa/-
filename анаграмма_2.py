# Данный файл создан Эльмирой Копаницей 24.01.2023 года по книге "Программируем на Пайтон" М.Доусона
# Доработайте игру "Анаграммы" так, чтобы к каждому слову полагалась подсказка.
# Игрок должен получать право на подсказку в том случае, если у него нет никаких предположений.
# Разработайте систему начисления очков, по которой игроки,
# отгадавшие слово без подсказки, получали бы больше тех, кто запросил подсказку.
import random

WORDS = ("питон", "анаграмма", "простая", "сложная", "ответ", "подстаканник")
word = random.choice(WORDS)
correct = word

jumble = ""
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position+1):]

print(
    """
            Добро пожаловать в игру 'Анаграммы'!
        Надо переставить буквы так, чтобы получилось осмысленное слово.
        У вас есть 3 подсказки, которыми вы можете воспользоваться.
        Однако, каждая подсказка забирает у вас 10 баллов, а попытка - 1 балл.
        Попробуйте отгадать слово, набрав максимальное количество балллов, 
        за наименьшее количество попыток.
    (Для выхода нажмите Enter, не вводя своей версии.)
    """
)
print("Вот анаграмма:", jumble, "\n\nВведите 'подсказка', если хотите ее получить.")
hint = 3
attempt = 0
game_ball = 100
guess = input("\nВаш вариант слова: ")
while guess.lower() != correct and guess.lower() != "":
    if guess.lower() == "подсказка":
        if hint != 0:
            if hint == 3:
                print("Последння буква слова -", correct[-1])
            if hint == 2:
                print("Третья буква слова -", correct[2])
            if hint == 1:
                print("Первая буква слова -", correct[0])
            hint -= 1
            game_ball -= 10
        else:
            print("\nУ вас не осталось подсказок.")

    attempt += 1
    game_ball -= 1
    print("Пока не угадали, попробуйте еще.")
    guess = input("\nВаш вариант слова: ")

if guess == correct:
    print(f"Да, именно так! Вы отгадали! Количество попыток {attempt}, баллов - {game_ball}.\n")
print("Спасибо за игру.")
input("\n\nНажмите Enter, чтобы выйти.")