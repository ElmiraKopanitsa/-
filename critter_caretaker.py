# Данный файл создан Эльмирой Копаницей 18.02.2023 года по книге "Программируем на Пайтон" М.Доусона
# Моя зверюшка
# Виртуальный питомец, о котором пользователь может заботиться
class Critter(object):
    '''Виртуальный питомец.'''
    def __init__(self, name, hunger=0, boredom=0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1

    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = 'прекрасно'
        elif 5 <= unhappiness <= 10:
            m = 'неплохо'
        elif 11 <= unhappiness <= 15:
            m = 'не сказать, чтобы хорошо'
        else:
            m = 'ужасно'
        return m

    def talk(self):
        print('Меня зовут', self.name, 'и я сейчас чувствую себя', self.mood, '\n')
        self.__pass_time()

    def eat(self, food=4):
        print('Мррр... спасибо!')
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self, fun=4):
        print('Уиии!')
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()

def main():
    crit_name = input('Как вы назовете свою зверюшку: ')
    crit = Critter(crit_name)

    choice = None
    while choice != '0':
        print(
        '''
        Моя зверюшка
        0 - выйти
        1 - узнать о самочувствии зверюшки
        2 - покормить зверюшку
        3 - поиграть со зверюшкой

        '''
    )
        choice = input('Ваш выбор (цифрой): ')
        print()
        if choice == '0':
            print('До свидания.')
        elif choice == '1':
            crit.talk()
        elif choice == '2':
            crit.eat()
        elif choice == '3':
            crit.play()
        else:
            print('Извините, в меню нет пункта', choice)

main()
input('\n\nНажмите Enter, чтобы выйти.')
