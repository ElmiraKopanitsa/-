# Данный файл создан Эльмирой Копаницей 25.02.2023 года по книге "Программируем на Пайтон" М.Доусона
# Спрайт-пицца
# Демонстрирует создание спрайта
from superwires import games
games.init(screen_width=640, screen_height=480, fps=50)
wall_image = games.load_image("elka.jpg", transparent=False)
games.screen.background = wall_image
pizza_image = games.load_image("Slice.jpeg")
pizza = games.Sprite(image=pizza_image, x=320, y=240)
games.screen.add(pizza)
games.screen.mainloop()