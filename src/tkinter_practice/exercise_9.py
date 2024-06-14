# Создайте GUI интерфейс для программы-каталога фильмов, книг и мультфильмов.
# Используйте виджеты Notebook и Treeview для вывода объектов разного типа на отдельных вкладках.
# Реализуйте всплывающее окно для вывода полной информации об издании.

import tkinter as tk
from tkinter import ttk


def create_tkinter_app():
    root = tk.Tk()
    root.title("Media catalog")
    root.geometry('800x500')

    notebook = ttk.Notebook(root)

    def display_tab1():
        frame = tk.Frame(notebook)
        notebook.add(frame, text="Фильмы")

        label = tk.Label(frame, text="Список фильмов")
        label.pack(pady=20)

        tree = ttk.Treeview(frame, columns=("Название", "Режиссёр", "Студия", "Год"), show="headings", height=17)
        tree.heading("Название", text="Название")
        tree.heading("Режиссёр", text="Режиссёр")
        tree.heading("Студия", text="Студия")
        tree.heading("Год", text="Год")

        tree.column("Название", width=210)
        tree.column("Режиссёр", width=170)
        tree.column("Студия", width=180)
        tree.column("Год", width=100, anchor='center')

        # ТЕСТОВОЕ НАПОЛНЕНИЕ
        tree.insert("", tk.END, values=("Области тьмы", "Нил Бёргер", "CBS Media Ventures, Netflix", 2011))
        tree.insert("", tk.END, values=("Джон Уик", "Чад Стахелски, Дэвид Литч", "Summit Entertainment", 2014))
        tree.insert("", tk.END, values=("Восставший из ада", " Клайв Баркер", "Sonar Entertainment", 1987))

        tree.pack()

    def display_tab2():
        frame = tk.Frame(notebook)
        notebook.add(frame, text="Книги")

        label = tk.Label(frame, text="Список книг")
        label.pack(pady=20)

        tree = ttk.Treeview(frame, columns=("Название", "Автор", "Издательство", "Год"), show="headings", height=17)
        tree.heading("Название", text="Название")
        tree.heading("Автор", text="Автор")
        tree.heading("Издательство", text="Издательство")
        tree.heading("Год", text="Год")

        tree.column("Название", width=210)
        tree.column("Автор", width=170)
        tree.column("Издательство", width=180, anchor='center')
        tree.column("Год", width=100, anchor='center')

        # ТЕСТОВОЕ НАПОЛНЕНИЕ
        tree.insert("", tk.END, values=("Война и мир", "Лев Толстой", "Азбука", 1869))
        tree.insert("", tk.END, values=("Преступление и наказание", "Федор Достоевский", "АСТ", 1866))
        tree.insert("", tk.END, values=("Мастер и Маргарита", "Михаил Булгаков", "Эксмо", 1966))

        # ДОДЕЛАТЬ!!!!!
        def show_details(event):
            item = tree.selection()[0]
            book_data = tree.item(item, "values")
            popup = tk.Toplevel(root)
            popup.title(f"Издание: {book_data[2]}")
            text = tk.Text(popup, wrap=tk.WORD)
            text.insert(tk.END, f"-----Подробности об издании-----")
            text.pack(expand=True, fill="both")

        tree.bind("<Button-1>", show_details)

        tree.pack()

    def display_tab3():
        frame = tk.Frame(notebook)
        notebook.add(frame, text="Мультфильмы")

        label = tk.Label(frame, text="Список мультфильмов")
        label.pack(pady=20)

        tree = ttk.Treeview(frame, columns=("Название", "Студия", "Год"), show="headings", height=17)
        tree.heading("Название", text="Название")
        tree.heading("Студия", text="Студия")
        tree.heading("Год", text="Год")

        tree.column("Название", width=240)
        tree.column("Студия", width=210)
        tree.column("Год", width=130, anchor='center')

        # ТЕСТОВОЕ НАПОЛНЕНИЕ
        tree.insert("", tk.END, values=("Тайна Коко", "Pixar, Walt Disney Pictures", 2017))
        tree.insert("", tk.END, values=("Золушка", "RKO Pictures", 1950))
        tree.insert("", tk.END, values=("Кот в сапогах", "DreamWorks Animation", 2011))

        tree.pack()

    display_tab1()
    display_tab2()
    display_tab3()

    notebook.pack(expand=True, fill='both')

    root.mainloop()


def main():
    create_tkinter_app()


if __name__ == '__main__':
    main()
