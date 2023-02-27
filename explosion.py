# Данный файл создан Эльмирой Копаницей 27.02.2023 года по книге "Программируем на Пайтон" М.Доусона
# Взрыв
# Демонстрирует создание анимации
from superwires import games
games.init(screen_width=1920, screen_height=1080, fps=50)

space_image = games.load_image("Space.jpg", transparent=0)
games.screen.background = space_image

explosion_files = ["16_1.jpg",
                   "16_2.jpg",
                   "16_3.jpg",
                   "16_4.jpg",
                   "16_5.jpg",
                   "16_6.jpg",
                   "16_7.jpg",
                   "16_7.jpg",
                   "16_8.jpg",
                   "16_9.jpg"]

explosion = games.Animation(images=explosion_files,
                            x=games.screen.width/2,
                            y=games.screen.height/2,
                            n_repeats=0,
                            repeat_interval=5)
games.screen.add(explosion)
games.screen.mainloop()