# Напишите GUI программу, которая позволяет пользователю выбрать цвет из палитры, и отображает его HEX-значение.

import tkinter as tk
from tkinter import colorchooser


def create_tkinter_app():
    root = tk.Tk()
    root.title("Color choosing")

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_width = 900
    window_height = 600
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)
    root.geometry(f'{window_width}x{window_height}+{x}+{y}')

    def choose_color():
        color = colorchooser.askcolor(title="Выбор цвета")
        if color[1]:
            color_label = tk.Label(root, text=f"Вы выбрали цвет {color[1]}")
            color_label.place(x=380, y=250)
            rectangle = tk.Canvas(root, width=165, height=43, bg=color[1])
            rectangle.place(x=370, y=290)

    choose_button = tk.Button(root, text="Выбрать цвет", command=choose_color)
    choose_button.place(x=405, y=200)

    root.mainloop()


def main():
    create_tkinter_app()


if __name__ == '__main__':
    main()
