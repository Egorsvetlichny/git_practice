# Напишите GUI калькулятор, который:
# -Выполняет основные арифметические операции – сложение, вычитание, деление и умножение.
# -Поддерживает операции с отрицательными числами, извлечение квадратного корня,
# деление с остатком и целочисленное деление.

# Кроме того, программа должна поддерживать очистку ввода.

import tkinter as tk


def create_tkinter_app():
    root = tk.Tk()
    root.title("GUI Калькулятор")

    root.grid_propagate(False)
    root.geometry('600x300')

    entry = tk.Entry(root)
    entry.place(x=200, y=47, width=200)

    # row 0
    button_1 = tk.Button(root, text='1', width=10, height=1)
    button_2 = tk.Button(root, text='2', width=10, height=1)
    button_3 = tk.Button(root, text='3', width=10, height=1)
    button_plus = tk.Button(root, text='+', width=10, height=1)
    button_int_div = tk.Button(root, text='//', width=10, height=1)
    button_1.place(x=80, y=110)
    button_2.place(x=170, y=110)
    button_3.place(x=260, y=110)
    button_plus.place(x=350, y=110)
    button_int_div.place(x=440, y=110)

    # row 1
    button_1 = tk.Button(root, text='4', width=10, height=1)
    button_2 = tk.Button(root, text='5', width=10, height=1)
    button_3 = tk.Button(root, text='6', width=10, height=1)
    button_plus = tk.Button(root, text='-', width=10, height=1)
    button_int_div = tk.Button(root, text='%', width=10, height=1)
    button_1.place(x=80, y=148)
    button_2.place(x=170, y=148)
    button_3.place(x=260, y=148)
    button_plus.place(x=350, y=148)
    button_int_div.place(x=440, y=148)

    # row 2
    button_1 = tk.Button(root, text='7', width=10, height=1)
    button_2 = tk.Button(root, text='8', width=10, height=1)
    button_3 = tk.Button(root, text='9', width=10, height=1)
    button_plus = tk.Button(root, text='*', width=10, height=1)
    button_int_div = tk.Button(root, text='№', width=10, height=1)
    button_1.place(x=80, y=186)
    button_2.place(x=170, y=186)
    button_3.place(x=260, y=186)
    button_plus.place(x=350, y=186)
    button_int_div.place(x=440, y=186)

    # row 3
    button_1 = tk.Button(root, text='C', width=10, height=1)
    button_2 = tk.Button(root, text='0', width=10, height=1)
    button_3 = tk.Button(root, text='=', width=10, height=1)
    button_plus = tk.Button(root, text='/', width=10, height=1)
    button_int_div = tk.Button(root, text='+/-', width=10, height=1)
    button_1.place(x=80, y=224)
    button_2.place(x=170, y=224)
    button_3.place(x=260, y=224)
    button_plus.place(x=350, y=224)
    button_int_div.place(x=440, y=224)

    root.mainloop()


def main():
    create_tkinter_app()


if __name__ == '__main__':
    main()
