# Создайте Tkinter интерфейс для программы заказа фруктов.
# Для вывода списка фруктов используйте виджет Combobox из модуля ttk.

import tkinter as tk
from tkinter import ttk


def create_tkinter_app():
    root = tk.Tk()
    root.title("Combobox fruits")

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_width = 900
    window_height = 600
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)
    root.geometry(f'{window_width}x{window_height}+{x}+{y}')

    fruits_list = ['Яблоки', 'Апельсины', 'Виноград', 'Персики', 'Клубника']

    combobox = ttk.Combobox(root, values=fruits_list)
    combobox.pack(pady=200)
    combobox.current(0)

    label = tk.Label(root, text=f"Выбрано: {combobox.get()}, 1 кг")
    label.place(x=385, y=240)

    def combobox_label_select(event):
        label.config(text=f"Выбрано: {combobox.get()}, 1 кг")

    combobox.bind("<<ComboboxSelected>>", func=combobox_label_select)

    def order_fruits():
        print(f"Заказали: {combobox.get()} - 1 кг")

    button = tk.Button(root, text="Заказать", command=order_fruits)
    button.place(x=420, y=280)

    root.mainloop()


def main():
    create_tkinter_app()


if __name__ == '__main__':
    main()
