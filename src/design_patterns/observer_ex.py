from abc import ABCMeta, abstractmethod


class IObservable(metaclass=ABCMeta):
    @abstractmethod
    def add_observer(self, observer: 'IObserver'):
        pass

    @abstractmethod
    def delete_observer(self, observer: 'IObserver'):
        pass

    @abstractmethod
    def notify(self):
        pass


class IObserver(metaclass=ABCMeta):
    def __init__(self, product: IObservable):
        self._product = product
        product.add_observer(self)

    @abstractmethod
    def update(self, price: int):
        pass


class RaceHorses(IObservable):
    def __init__(self, price: int):
        self.__price = price
        self.__observers = []

    def change_price(self, new_price):
        self.__price = new_price
        self.notify()

    def add_observer(self, observer: 'IObserver'):
        self.__observers.append(observer)

    def delete_observer(self, observer: 'IObserver'):
        self.__observers.remove(observer)

    def notify(self):
        for observer in self.__observers:
            observer.update(self.__price)


class RichAuctioneer(IObserver):
    def update(self, new_price):
        if new_price < 10_000_000:
            print(f'Богатый аукционер купил скаковую лошадь за {new_price}')
            self._product.delete_observer(self)
        else:
            print(f'Богатый аукционер отказался покупать скаковую лошадь за {new_price}')


class AVGIncomeAuctioneer(IObserver):
    def update(self, new_price):
        if new_price < 5_000_000:
            print(f'Средних доходов аукционер купил скаковую лошадь за {new_price}')
            self._product.delete_observer(self)
        else:
            print(f'Средних доходов аукционер отказался покупать скаковую лошадь за {new_price}')


class PoorAuctioneer(IObserver):
    def update(self, new_price):
        if new_price < 100_000:
            print(f'Бедный аукционер купил скаковую лошадь за {new_price}')
            self._product.delete_observer(self)
        else:
            print(f'Бедный аукционер отказался покупать скаковую лошадь за {new_price}')


if __name__ == '__main__':
    race_horses = RaceHorses(15_000_000)

    poor_auc = PoorAuctioneer(race_horses)
    avg_income_auc = AVGIncomeAuctioneer(race_horses)
    rich_auc = RichAuctioneer(race_horses)

    race_horses.change_price(11_000_000)

    print()

    race_horses.change_price(9_000_000)

    print()

    race_horses.change_price(3_000_000)

    print()

    race_horses.change_price(95_000)

    # ничего не происходит, т.к. каждый аукционер уже купил скаковую лошадь по доступной для себя цене
    race_horses.change_price(1_000_000)
