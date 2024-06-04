# Функция search из библиотеки googlesearch позволяет делать запрос в поисковик прямо в консоли, не открывая браузер.

import googlesearch


def make_query(query: str) -> None:
    for i in googlesearch.search(query, num_results=5):
        print(i)


def main():
    user_query = 'top the best developers ever'
    make_query(user_query)


if __name__ == '__main__':
    main()
