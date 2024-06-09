# Напишите программу, которая использует виджеты Spinbox для получения двух чисел a и b (0 <= a <= 100, 0 <= b <= 100),
# а затем выводит сумму всех целых чисел в диапазоне от a до b включительно.

import tkinter as tk


def create_tkinter_app():
    root = tk.Tk()
    root.title("Sum two numbers")

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_width = 900
    window_height = 600
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)
    root.geometry(f'{window_width}x{window_height}+{x}+{y}')

    spinbox1 = tk.Spinbox(root, from_=0, to=100, increment=1)
    spinbox2 = tk.Spinbox(root, from_=0, to=100, increment=1)
    spinbox1.place(x=370, y=190)
    spinbox2.place(x=370, y=230)

    def evaluate_sum():
        num1, num2 = int(spinbox1.get()), int(spinbox2.get())
        if num1 <= num2 and 0 <= num1 <= 100 and 0 <= num2 <= 100:
            sum_of_values = sum(range(num1, num2 + 1))
            label.config(text=f"Сумма чисел в диапазоне от {num1} до {num2}: {sum_of_values}")
            label.place(x=330, y=280)

        else:
            label.config(text=f"Неверно указан диапазон!")
            label.place(x=363, y=280)

    label = tk.Label(root, text='')

    button = tk.Button(root, text="Вычислить сумму", command=evaluate_sum)
    button.place(x=383, y=330)

    root.mainloop()


def main():
    create_tkinter_app()


if __name__ == '__main__':
    main()
