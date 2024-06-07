# Создайте индикатор выполнения задачи с помощью виджета Progressbar из модуля ttk.
# Индикатор должен обнуляться спустя 5 секунд.

import time
import tkinter as tk
from tkinter import ttk


def create_tkinter_app():
    root = tk.Tk()
    root.title("Progressbar")

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_width = 900
    window_height = 600
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)
    root.geometry(f'{window_width}x{window_height}+{x}+{y}')

    progressbar = ttk.Progressbar(root, orient="horizontal", length=200, mode="determinate")
    progressbar.pack(pady=200)
    progressbar["value"] = 1

    def update_progressbar():
        for i in range(2, 101):
            progressbar["value"] = i
            root.update_idletasks()
            time.sleep(0.1)

    update_progressbar()

    def reset_progressbar():
        progressbar["value"] = 0

    root.after(5000, func=reset_progressbar)

    root.mainloop()


def main():
    create_tkinter_app()


if __name__ == '__main__':
    main()
