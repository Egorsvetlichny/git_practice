# Создайте Tkinter интерфейс для программы, которая получает от пользователя текст с помощью виджетов Entry и Button,
# а затем выводит полученную строку в терминале.

import tkinter as tk


def create_tkinter_app():
    root = tk.Tk()
    root.title("Вывод пользовательской строки в консоль")

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_width = 900
    window_height = 600
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)
    root.geometry(f'{window_width}x{window_height}+{x}+{y}')

    entry1 = tk.Entry(root)
    entry1.config(width=60)
    entry1.place(x=275, y=200)

    button1 = tk.Button(root, text="Отправить", command=lambda: print(entry1.get()))
    button1.config(width="15", height="3", activebackground="black")
    button1.place(x=390, y=240)

    root.mainloop()


def main():
    create_tkinter_app()


if __name__ == '__main__':
    main()
