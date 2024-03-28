from abc import ABCMeta, abstractmethod


class ICurrency(metaclass=ABCMeta):
    @abstractmethod
    def get_count_money(self):
        pass

    @abstractmethod
    def get_adjust_info(self):
        pass


class RusCurrency(ICurrency):
    def __init__(self, count_money):
        self.__count_money = count_money

    def get_count_money(self):
        return self.__count_money

    def get_adjust_info(self):
        print("Регулировка измерений в Российской валюте.", end=' ')


class UsaCurrency(ICurrency):
    def __init__(self, count_money):
        self.__count_money = count_money

    def get_count_money(self):
        return self.__count_money

    def get_adjust_info(self):
        print("Регулировка измерений в валюте США.")


class AdapterForRusCurrency(RusCurrency, ICurrency):
    def __init__(self, count_money):
        super().__init__(count_money)

    def get_count_money(self):
        return super().get_count_money() * 0.010802

    def get_adjust_info(self):
        super().get_adjust_info()
        print("Использование адаптера для конвертации российской валюты в доллар США")


if __name__ == '__main__':
    money = 65_000

    usa_currency = UsaCurrency(money)
    rus_currency = AdapterForRusCurrency(money)

    print(f'{money} долларов США в долларах США: {usa_currency.get_count_money()}')
    print(f'{money} российских рублей в долларах США: {rus_currency.get_count_money()}')

    print()

    usa_currency.get_adjust_info()
    rus_currency.get_adjust_info()
