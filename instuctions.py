# Данный файл создан Эльмирой Копаницей 02.02.2023 года по книге "Программируем на Пайтон" М.Доусона
# Инструкция
# Демоснтрирует, как создавать собственные инструкции
def instructions():
    """Выводит на экран инструкцию для игрока."""
    print(
        """
        Добро пожаловать на ринг грандиознейших интеллектуальных состязаний всех времен.
        Твой мозг и мой процессор сойдутся в схватке за доской игры "Крестики-нолики".
        Чтобы сделать ход, введи число от 0 до 8. Числа однозначно соответствуют полям
        доски - так, как показано ниже:
        0 | 1 | 2
        ----------
        3 | 4 | 5
        ----------
        6 | 7 | 8

        Приготовься к бою, жалкий белквоый человечешка. Вот-вот начнется решающее сражение.\n

        """
    )
# основная часть
print('Это инструкция для игры "Крестики-нолики":')
instructions()
print('Это опять та же самая инструкция:')
instructions()
print('Надеюсь, теперь смысл игры ясен.')
input('\n\nНажмите Enter, чтобы выйти.')