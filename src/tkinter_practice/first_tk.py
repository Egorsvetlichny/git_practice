# Первое GUI-приложение на tkinter

import tkinter

root = tkinter.Tk()
root.title("Первое приложение на tkinter")

# root.geometry("900x600")
# Позиционирование окна в центре экрана
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = 900
window_height = 600
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
root.geometry(f'{window_width}x{window_height}+{x}+{y}')

root.mainloop()
