# Второе GUI-приложение на tkinter. Связывание виджетов с функциями

import tkinter as tk
from functools import partial

root = tk.Tk()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = 900
window_height = 600
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
root.geometry(f'{window_width}x{window_height}+{x}+{y}')


def say_hello_world():
    print("Hello, world!")


def say_hi(event=None):
    print("Hi, everyone!")


def say_hello_name(name):
    print("Hi, {name}!".format(name=name))


# Назначение кнопке функции с помощью метода command()
button1 = tk.Button(root, text="Кнопка 1", command=say_hello_world)
button1.config(width="15", height="3", activebackground="black")
button1.place(x=380, y=130)

# Назначение кнопке функции с помощью метода bind()
button2 = tk.Button(root, text="Кнопка 2")
button2.bind("<Button-1>", say_hi)
button2.config(width="15", height="3", activebackground="black")
button2.place(x=380, y=230)

# Назначение кнопке анонимной функции
button3 = tk.Button(root, text="Кнопка 3", command=lambda: print("Сработала анонимная функция!"))
button3.config(width="15", height="3", activebackground="black")
button3.place(x=380, y=330)

# Связывание кнопки с частично примененной функцией
button4 = tk.Button(root, text="Кнопка 4", command=partial(say_hello_name, 'dear friend'))
button4.config(width="15", height="3", activebackground="black")
button4.place(x=380, y=430)

root.mainloop()
