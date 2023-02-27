# Данный файл создан Эльмирой Копаницей 27.02.2023 года по книге "Программируем на Пайтон" М.Доусона
# Паника в пиццерии
# Игрок должен ловить падающую пиццу, пока она не достигла земли
from superwires import games, color
import random

games.init(screen_width=1920, screen_height=1080, fps=50)

class Pan(games.Sprite):
    """Сковорода, в которую игрок может ловить падающую пиццу."""
    image = games.load_image("Сковорода.jpeg")

    def __init__(self):
        """Инициализирует объект Pan и создает объект Text для отображения счета."""
        super(Pan, self).__init__(image=Pan.image,
                                  x=games.mouse.x,
                                  bottom=games.screen.height)
        self.score = games.Text(value=0, size=25, color=color.black)
        games.screen.add(self.score)

    def update(self):
        """Передвигает объект по горизонтали в точку с абсциссой, как у указателя мыши."""
        self.x = games.mouse.x
        if self.left < 0:
            self.left = 0
        if self.right > games.screen.width:
            self.right = games.screen.width
        self.check_catch()
    
    def check_catch(self):
        """Проверяет, поймал ли игрок падающую пиццу."""
        for pizza in self.overlapping_sprites:
            self.score.value += 10
            self.score.x = games.screen.width - 50
            self.score.y = games.screen.height/12
            pizza.handle_caught()


class Pizza(games.Sprite):
    """Пицца, падающая на землю."""
    image = games.load_image("Slice.jpeg")
    speed = 5
    def __init__(self, x, y = 90):
        """Инициализирует объект Pizza."""
        super(Pizza, self).__init__(image=Pizza.image,
                                    x=x, y=y, dy=Pizza.speed)
        
    def update(self):
        """Проверяет, не коснулась ли нижняя кромка спрайта нижней границы экрана."""
        if self.bottom > games.screen.height:
            self.end_game()
            self.destroy()

    def handle_caught(self):
        """Разрушает объект, пойманный игроком."""
        self.destroy()

    def end_game(self):
        """Завершает игру."""
        end_message = games.Message(value="Game Over",
                                    size=90,
                                    color=color.black,
                                    x=games.screen.width/2,
                                    y=games.screen.height/2,
                                    lifetime=5*games.screen.fps,
                                    after_death=games.screen.quit)
        games.screen.add(end_message)


class Chef(games.Sprite):
    """Кулинар, который двигаясь влево-вправо разбрасывает пиццу."""
    image = games.load_image("Chef.jpeg")

    def __init__(self, y=55, speed=2, odds_change=150):
        """Инициализирует объект Chef."""
        super(Chef, self).__init__(image=Chef.image,
                                   x=games.screen.width/2,
                                   y=y, dx=speed)
        self.odds_change = odds_change
        self.time_till_drop = 0

    def update(self):
        """Определяет, надо ли сменить направление."""
        if self.left < 0 or self.right > games.screen.width:
            self.dx = -self.dx
        elif random.randrange(self.odds_change) == 0:
            self.dx = -self.dx
        self.check_drop()
    
    def check_drop(self):
        """Уменьшает интервал ожидания на единицу или сбрасывает очередную пиццу
         и восстанавливает исходный интервал."""
        if self.time_till_drop > 0:
            self.time_till_drop -= 1
        else:
            new_pizza = Pizza(x=self.x)
            games.screen.add(new_pizza)
            # вне зависимости от скорости падения пиццы "зазор" между падающими кусками принимается равным 30% каждого из них по высоте
            self.time_till_drop = int(new_pizza.height * 1.3 / Pizza.speed) + 1

def main():
    """Собственно игровой процесс."""
    wall_image = games.load_image("Море.jpg", transparent=False)
    games.screen.background = wall_image
    the_chef = Chef()
    games.screen.add(the_chef)
    the_pan = Pan()
    games.screen.add(the_pan)
    games.mouse.is_visible= False
    games.screen.event_grab = True
    games.screen.mainloop()

main()