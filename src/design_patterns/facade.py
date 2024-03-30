class ReleaseIronman:
    def release_ironman(self):
        print('Выпуск железного человека.')

    def publish_info(self):
        print('Публикация информации о выпускаемом железном человеке.')


class DeliveryIronmanToArmy:
    def delivery_ironman(self):
        print('Поставка железного человека на вооружение.')

    def publish_info(self):
        print('Публикация информации о поставке железного человека на военную службу.')


class ModifyIronman:
    def modify_ironman(self):
        print('Модификация железного человека.')

    def publish_info(self):
        print('Публикация информации о модификации железного человека.')


class FacadeIronman:
    def __init__(self):
        self._release_ironman = ReleaseIronman()
        self._delivery_ironman = DeliveryIronmanToArmy()
        self._modify_ironman = ModifyIronman()

    def act_ironman(self):
        print('---Метод фассада 1---')
        self._release_ironman.release_ironman()
        self._delivery_ironman.delivery_ironman()
        self._modify_ironman.modify_ironman()

    def publish_info(self):
        print('---Метод фассада 2---')
        self._release_ironman.publish_info()
        self._delivery_ironman.publish_info()
        self._modify_ironman.publish_info()


if __name__ == '__main__':
    facade_ironman = FacadeIronman()

    facade_ironman.act_ironman()

    print()

    facade_ironman.publish_info()
