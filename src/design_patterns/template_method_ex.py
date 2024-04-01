from abc import ABCMeta, abstractmethod


class Ironman(metaclass=ABCMeta):
    @abstractmethod
    def body_install(self):
        pass

    @abstractmethod
    def head_install(self):
        pass

    def arms_install(self):
        print("Установка рук;")

    def legs_install(self):
        print("Установка ног;")

    def weapon_install(self):
        pass

    def wings_install(self):
        pass

    @abstractmethod
    def get_info(self):
        pass

    def create_ironman(self):
        self.get_info()
        self.body_install()
        self.head_install()
        self.arms_install()
        self.legs_install()
        self.weapon_install()
        self.wings_install()


class FullIronman(Ironman):
    def get_info(self):
        print("Произведена надёжная сборка железного человека: ")

    def head_install(self):
        print("Полная установка головы железного человека;")

    def body_install(self):
        print("Полная установка корпуса железного человека;")

    def arms_install(self):
        print("Полная установка рук;")

    def legs_install(self):
        print("Полная установка ног;")

    def wings_install(self):
        print("Полная установка крыльев;")

    def weapon_install(self):
        print("Полная установка оружия;")


class FastIronman(Ironman):
    def get_info(self):
        print("Произведена скоростная сборка железного человека: ")

    def head_install(self):
        print("Быстрая установка головы;")

    def body_install(self):
        print("Быстрая установка туловища;")


if __name__ == '__main__':
    fast_ironman = FastIronman()
    fast_ironman.create_ironman()

    print()

    full_ironman = FullIronman()
    full_ironman.create_ironman()
