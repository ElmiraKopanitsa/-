# Данный файл создан Эльмирой Копаницей 18.02.2023 года по книге "Программируем на Пайтон" М.Доусона
# Зверюшка со свойствами
# Демонстрирует свойства
class Critter(object):
    '''Виртуальный питомец.'''
    def __init__(self, name):
        print('Появилась на свет новая зверюшка!')
        self.__name = name
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, new_name):
        if new_name == '':
            print('Имя зверюшки не может быть пустой строкой.')
        else:
            self.__name = new_name
            print('Имя успешно изменено.')
    
    def talk(self):
        print('\nПривет, меня зовут', self.name)

# основная часть
crit = Critter('Бобик')
crit.talk()
print('Мою зверюшку зовут', end=' ')
print(crit.name)
print('Попробую поменять имя зверюшки на Мурзик...')
crit.name = 'Мурзик'
print('Мою зверюшку зовут', end=' ')
print(crit.name)
print('Попробую изменить имя зверюшки на пустую строку...')
crit.name = ''
print('Мою зверюшку зовут', end = ' ')
print(crit.name)
input('\n\nНажмите Enter, чтобы выйти.')
