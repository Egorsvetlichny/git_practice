# Создайте интерфейс для программы, которая изменяет текст виджета Label после нажатия на кнопку.

import tkinter as tk


def create_tkinter_app():
    root = tk.Tk()
    root.title("Изменение текса объекта label")

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_width = 900
    window_height = 600
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)
    root.geometry(f'{window_width}x{window_height}+{x}+{y}')

    def change_label():
        label.config(text="Это новый текст!")

    label = tk.Label(root, text="Измени этот текст")
    label.place(x=400, y=270)
    button = tk.Button(root, text="Нажми на кнопку!", command=change_label)
    button.place(x=395, y=300)

    root.mainloop()


def main():
    create_tkinter_app()


if __name__ == '__main__':
    main()
