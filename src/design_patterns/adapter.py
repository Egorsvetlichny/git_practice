from abc import ABCMeta, abstractmethod


class ICurrency(metaclass=ABCMeta):
    @abstractmethod
    def get_count_money(self):
        pass


class RubCurrency(ICurrency):
    def __init__(self, count_money):
        self.__count_money = count_money

    def get_count_money(self):
        return self.__count_money


class UsdCurrency(ICurrency):
    def __init__(self, count_money):
        self.__count_money = count_money

    def get_count_money(self):
        return self.__count_money


class KrwCurrency(ICurrency):
    def __init__(self, count_money):
        self.__count_money = count_money

    def get_count_money(self):
        return self.__count_money


class AdapterForRubCurrency(ICurrency):
    def __init__(self, rub_currency: RubCurrency):
        self.__rub_currency = rub_currency

    def get_count_money(self):
        return self.__rub_currency.get_count_money() * 0.010802


class AdapterForKrwCurrency(ICurrency):
    def __init__(self, krw_currency: KrwCurrency):
        self.__krw_currency = krw_currency

    def get_count_money(self):
        return self.__krw_currency.get_count_money() * 0.000747


class AdapterForUsdToRub(ICurrency):
    def __init__(self, usd_currency: UsdCurrency):
        self.__usd_currency = usd_currency

    def get_count_money(self):
        return self.__usd_currency.get_count_money() * 92.57


if __name__ == '__main__':
    money = 100

    rub_currency = AdapterForRubCurrency(RubCurrency(money))
    usd_currency = UsdCurrency(money)
    krw_currency = AdapterForKrwCurrency(KrwCurrency(money))

    print(f"100 рублей в долларах равно: {rub_currency.get_count_money()}")
    print(f"100 долларов в долларах равно: {usd_currency.get_count_money()}")
    print(f"100 вон в долларах равно: {krw_currency.get_count_money()}")

    print()

    print(f"100 долларов в рублях равно: {AdapterForUsdToRub(UsdCurrency(money)).get_count_money()}")
