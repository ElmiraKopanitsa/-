# Данный файл создан Эльмирой Копаницей 20.02.2023 года по книге "Программируем на Пайтон" М.Доусона
# Бесполезные кнопки - 2
# Демонстрирует создание класса в оконном приложении на основе tkinter
from tkinter import *
class Application(Frame):
    """GUI-приложение с тремя кнопками."""
    def __init__(self, master):
        """Инициализирует рамку."""
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgest()
    
    def create_widgest(self):
        """Создает три бесполезные кнопки."""
        # первая кнопка
        self.bttn1 = Button(self, text = "Я ничего не делаю!")
        self.bttn1.grid()
        # вторая кнопка
        self.bttn2 = Button(self)
        self.bttn2.grid()
        self.bttn2.configure(text="И я тоже!")
        # третья кнопка
        self.bttn3 = Button(self)
        self.bttn3.grid()
        self.bttn3["text"] = "И я!"

# основная часть
root = Tk()
root.title("Бесполезные кнопки - 2")
root.geometry("200x85")
app = Application(root)
root.mainloop()
