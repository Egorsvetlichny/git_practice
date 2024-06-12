# Напишите GUI калькулятор, который:
# -Выполняет основные арифметические операции – сложение, вычитание, деление и умножение.
# -Поддерживает операции с отрицательными числами, извлечение квадратного корня,
# деление с остатком и целочисленное деление.

# Кроме того, программа должна поддерживать очистку ввода.

import tkinter as tk
import re

import numexpr


def create_tkinter_app():
    root = tk.Tk()
    root.title("GUI Калькулятор")

    root.geometry('600x300')
    root.resizable(False, False)

    entry = tk.Entry(root, textvariable=tk.StringVar(value='0'))
    entry.place(x=170, y=47, width=260)

    def insert_text(button):
        button_text = button.cget('text')

        if button_text.isdigit() and entry.get() == '0':
            entry.delete(0, tk.END)

        math_operation = ('+', '-', '*', '/', '//', '%', '^')
        if entry.get() == 'Неверное математическое выражение!':
            if button_text in math_operation or button_text == '√':
                entry.delete(0, tk.END)
                entry.insert(tk.END, '0' + button_text)
            elif button_text.isdigit():
                entry.delete(0, tk.END)
                entry.insert(tk.END, button_text)
            else:
                pass
        elif button_text in math_operation and entry.get()[-1] in math_operation:
            if button_text != '//':
                entry.delete(len(entry.get()) - 1, tk.END)
                entry.insert(tk.END, button_text)
            else:
                entry.delete(len(entry.get()) - 2, tk.END)
                entry.insert(tk.END, button_text)
        elif button_text == 'C':
            entry.delete(0, tk.END)
            entry.insert(tk.END, '0')
        elif button_text == '=':
            expression = entry.get().replace('^', '**')
            entry.delete(0, tk.END)
            try:
                result = str(numexpr.evaluate(expression))
                entry.insert(tk.END, result)
                return result
            except (ValueError, ZeroDivisionError, TypeError, Exception):
                entry.insert(tk.END, "Неверное математическое выражение!")
        # ДОДЕЛАТЬ!
        elif button_text == '√':
            if entry.get()[-1] in math_operation:
                entry.insert(tk.END, button_text)
        else:
            entry.insert(tk.END, button_text)

    # row 0
    button_1 = tk.Button(root, text='1', width=10, height=1, command=lambda: insert_text(button_1))
    button_2 = tk.Button(root, text='2', width=10, height=1, command=lambda: insert_text(button_2))
    button_3 = tk.Button(root, text='3', width=10, height=1, command=lambda: insert_text(button_3))
    button_plus = tk.Button(root, text='+', width=10, height=1, command=lambda: insert_text(button_plus))
    button_int_div = tk.Button(root, text='//', width=10, height=1, command=lambda: insert_text(button_int_div))
    button_1.place(x=80, y=110)
    button_2.place(x=170, y=110)
    button_3.place(x=260, y=110)
    button_plus.place(x=350, y=110)
    button_int_div.place(x=440, y=110)

    # # row 1
    button_4 = tk.Button(root, text='4', width=10, height=1, command=lambda: insert_text(button_4))
    button_5 = tk.Button(root, text='5', width=10, height=1, command=lambda: insert_text(button_5))
    button_6 = tk.Button(root, text='6', width=10, height=1, command=lambda: insert_text(button_6))
    button_minus = tk.Button(root, text='-', width=10, height=1, command=lambda: insert_text(button_minus))
    button_mod = tk.Button(root, text='%', width=10, height=1, command=lambda: insert_text(button_mod))
    button_4.place(x=80, y=148)
    button_5.place(x=170, y=148)
    button_6.place(x=260, y=148)
    button_minus.place(x=350, y=148)
    button_mod.place(x=440, y=148)

    # # row 2
    button_7 = tk.Button(root, text='7', width=10, height=1, command=lambda: insert_text(button_7))
    button_8 = tk.Button(root, text='8', width=10, height=1, command=lambda: insert_text(button_8))
    button_9 = tk.Button(root, text='9', width=10, height=1, command=lambda: insert_text(button_9))
    button_mult = tk.Button(root, text='*', width=10, height=1, command=lambda: insert_text(button_mult))
    button_root = tk.Button(root, text='√', width=10, height=1, command=lambda: insert_text(button_root))
    button_7.place(x=80, y=186)
    button_8.place(x=170, y=186)
    button_9.place(x=260, y=186)
    button_mult.place(x=350, y=186)
    button_root.place(x=440, y=186)

    # # row 3
    button_c = tk.Button(root, text='C', width=10, height=1, command=lambda: insert_text(button_c))
    button_0 = tk.Button(root, text='0', width=10, height=1, command=lambda: insert_text(button_0))
    button_eq = tk.Button(root, text='=', width=10, height=1, command=lambda: insert_text(button_eq))
    button_float_div = tk.Button(root, text='/', width=10, height=1, command=lambda: insert_text(button_float_div))
    button_plus_minus = tk.Button(root, text='^', width=10, height=1, command=lambda: insert_text(button_plus_minus))
    button_c.place(x=80, y=224)
    button_0.place(x=170, y=224)
    button_eq.place(x=260, y=224)
    button_float_div.place(x=350, y=224)
    button_plus_minus.place(x=440, y=224)

    root.mainloop()


def main():
    create_tkinter_app()


if __name__ == '__main__':
    main()
