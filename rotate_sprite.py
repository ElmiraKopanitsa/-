# Данный файл создан Эльмирой Копаницей 27.02.2023 года по книге "Программируем на Пайтон" М.Доусона
# Крутящийся спрайт
# Демонстрирует вращение спрайта
from superwires import games
games.init(screen_width=1920, screen_height=1080, fps=50)


class Ship(games.Sprite):
    """Вращающийся космический корабль."""
    def update(self):
        if games.keyboard.is_pressed(games.K_RIGHT):
            self.angle += 1
        if games.keyboard.is_pressed(games.K_LEFT):
            self.angle -= 1
        if games.keyboard.is_pressed(games.K_1):
            self.angle = 0
        if games.keyboard.is_pressed(games.K_2):
            self.angle = 90
        if games.keyboard.is_pressed(games.K_3):
            self.angle = 180
        if games.keyboard.is_pressed(games.K_4):
            self.angle = 270


def main():
    space_image = games.load_image("Space.jpg", transparent=False)
    games.screen.background = space_image
    ship_image = games.load_image("Spaceship.jpeg")
    the_ship = Ship(image=ship_image,
                    x=games.screen.width/2,
                    y=games.screen.height/2)
    games.screen.add(the_ship)
    games.screen.mainloop()


main()