from abc import ABCMeta, abstractmethod


class ISite(metaclass=ABCMeta):
    @abstractmethod
    def get_page(self, num: int):
        pass


class MySite(ISite):
    def get_page(self, num: int):
        return f'Cтраница {num}'


class ProxySite(ISite):
    def __init__(self, site: ISite):
        self.__site = site
        self.__cache = {}

    def get_page(self, num: int):
        page = ''
        if self.__cache.get(num) is not None:
            page = "Это страница из кэша: " + self.__cache[num]
        else:
            page = self.__site.get_page(num)
            self.__cache[num] = page

        return page


if __name__ == '__main__':
    site = MySite()
    proxy_site = ProxySite(site)

    print(proxy_site.get_page(1))
    print(proxy_site.get_page(2))
    print(proxy_site.get_page(3))

    print()

    print(proxy_site.get_page(1))
    print(proxy_site.get_page(2))
