# Напишите программу для оценки сервиса по шкале от 0 до 100. Используйте виджет Scale (ttk модуль).

import tkinter as tk


def create_tkinter_app():
    root = tk.Tk()
    root.title("Оценка сервиса от 0 до 100")

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_width = 900
    window_height = 600
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)
    root.geometry(f'{window_width}x{window_height}+{x}+{y}')

    def update_label(value):
        label.config(text=label_text + value)

    scale = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, command=update_label)
    scale.place(x=370, y=235)

    label_text = f"Ваша оценка: "
    label = tk.Label(root, text=label_text)
    label.place(x=380, y=200)

    root.mainloop()


def main():
    create_tkinter_app()


if __name__ == '__main__':
    main()
