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

# Размещение элементов интерфейса в Tkinter

# Пример использования pack:
label1 = tkinter.Label(root, text="Это пример использования pack()")
label1.pack()
button1 = tkinter.Button(root, text="Нажми!")
button1.pack()

# Пример использования place:
label1 = tkinter.Label(root, text="Это пример использования place()")
label1.place(x=350, y=100)
button1 = tkinter.Button(root, text="Кликни!")
button1.place(x=420, y=125)

# Пример использования grid:
frame = tkinter.Frame(root)
frame.pack(expand=True)
label1 = tkinter.Label(frame, text="Имя:")
label1.grid(row=0, column=0)
entry1 = tkinter.Entry(frame)
entry1.grid(row=0, column=1)
label2 = tkinter.Label(frame, text="Email:")
label2.grid(row=1, column=0)
entry2 = tkinter.Entry(frame)
entry2.grid(row=1, column=1)
button1 = tkinter.Button(frame, text="Нажми на кнопку!")
button1.grid(row=2, column=1)
root.update_idletasks()

root.mainloop()
