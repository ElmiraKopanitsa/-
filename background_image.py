# Данный файл создан Эльмирой Копаницей 25.02.2023 года по книге "Программируем на Пайтон" М.Доусона
# Фоновая картинка
# Демонстрирует назначение фоновой картинки для графического экрана
from superwires import games
games.init(screen_width=640, screen_height=480, fps=50)
wall_image = games.load_image("Ветка.jpeg", transparent=False)
games.screen.background = wall_image
games.screen.mainloop()