# Данный файл создан Эльмирой Копаницей 27.02.2023 года по книге "Программируем на Пайтон" М.Доусона
# Читаю с клавиатуры
# Демонстрирует чтение клавиатурного ввода
from superwires import games
games.init(screen_width=1920, screen_height=1080, fps=50)


class Spaceship(games.Sprite):
    """Подвижный корабль."""
    def update(self):
        """Перемещает корабль определенным образом, исходя из нажатых клавиш."""
        if games.keyboard.is_pressed(games.K_w):
            self.y -= 1
        if games.keyboard.is_pressed(games.K_s):
            self.y += 1
        if games.keyboard.is_pressed(games.K_a):
            self.x -= 1
        if games.keyboard.is_pressed(games.K_d):
            self.x += 1

def main():
    space_image = games.load_image("Space.jpg", transparent=False)
    games.screen.background = space_image
    spaceship_image = games.load_image("Spaceship.jpeg")
    the_ship = Spaceship(image=spaceship_image,
                         x=games.screen.width/2,
                         y=games.screen.height/2)
    games.screen.add(the_ship)
    games.screen.mainloop()

main()
