# schedule - пакет, который позволяет планировать задачи и повторять их через промежуток времени.

# Главный его плюс в том, что он максимально интуитивный и имеет гибкий функционал.
# Также, schedule не требует внешних зависимостей и сам в целом легковесный.

import schedule


def drink():
    print("drink")


def sleep():
    print("sleep")


def eat():
    print("eat")


def work():
    print("work")


def play():
    print("play")


def relax():
    print("relax")


def main():
    schedule.every(3).seconds.do(drink)
    schedule.every().minutes.do(sleep)
    schedule.every().hours.do(eat)
    schedule.every().day.at("10:30").do(work)
    schedule.every().monday.do(play)
    schedule.every().wednesday.at("18:00").do(relax)

    while True:
        schedule.run_pending()


if __name__ == '__main__':
    main()
