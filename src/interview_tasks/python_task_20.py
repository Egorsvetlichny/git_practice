# В отличие от объявления return в функции, где возвращается один объект,
# yield при каждом вызове функции генерирует новый объект.
# Фактически это дает возможность использовать генераторы в циклах.
# Самая важная причина применения такой инструкции - экономия памяти,
# когда не требуется сохранять всю последовательность, а можно получать ее элементы по одному.
#
# Ученик написал генератор show_letters(some_str), выводящий все символы строки на печать,
# но только в том случае, если они являются буквами (остальные игнорируются).
# Сократите код функции.
#
# Код – IDE
# ---
# def show_letters(some_str):
#     clean_str = ''.join([letter for letter in some_str if letter.isalpha()])
#     for symbol in clean_str:
#         yield symbol

# Решение
def show_letters(some_str):
    yield from ''.join([letter for letter in some_str if letter.isalpha()])


if __name__ == '__main__':
    random_str = show_letters('A!123d d3f 09fs _ re3 2 e/ 3d.')
    print(next(random_str))
    print(next(random_str))
    print(next(random_str))
    print(next(random_str))
    print(next(random_str))
    print(next(random_str))
    print(next(random_str))
    print(next(random_str))
    print(next(random_str))
    print(next(random_str))
    # print(next(random_str)) бросает исключение StopIteration
