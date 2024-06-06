# Создайте интерфейс для программы, которая получает от пользователя многострочный текст в виджете Text
# и выводит в виджетах Label количество слов и символов.

import tkinter as tk


def create_tkinter_app():
    root = tk.Tk()
    root.title("Подсчёт слов и символов в тексте")

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_width = 900
    window_height = 600
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)
    root.geometry(f'{window_width}x{window_height}+{x}+{y}')

    text = tk.Text(root, width=40, height=10)
    text.place(x=0, y=0)
    text.insert(tk.END, "Человек в черном скрывался в пустыне, а стрелок преследовал его.")

    label1_text = "Количество слов: "
    label2_text = "Количество символов: "
    label1 = tk.Label(root, text=label1_text)
    label1.place(x=370, y=200)
    label2 = tk.Label(root, text=label2_text)
    label2.place(x=370, y=235)

    def count_words_and_chars():
        label1.config(text=label1_text + str(len(text.get("1.0", tk.END).split())))
        label2.config(text=label2_text + str(len(text.get("1.0", tk.END))))

    button = tk.Button(root, text="Подсчитать", command=count_words_and_chars)
    button.place(x=395, y=275)

    root.mainloop()


def main():
    create_tkinter_app()


if __name__ == '__main__':
    main()
