class Ironman:
    def release(self):
        pass


class RusIronman(Ironman):
    def release(self):
        print("Released new Russian Ironman")

    def __eq__(self, other):
        if isinstance(other, RusIronman):
            return True
        return False


class JapIronman(Ironman):
    def release(self):
        print("Released new Japan Ironman")


class UsaIronman(Ironman):
    def release(self):
        print("Released new American Ironman")


class IronmanFactory:
    def create(self) -> Ironman:
        pass


class RusIronmanFactory(IronmanFactory):
    def create(self) -> Ironman:
        return RusIronman()


class JapIronmanFactory(IronmanFactory):
    def create(self) -> Ironman:
        return JapIronman()


class UsaIronmanFactory(IronmanFactory):
    def create(self) -> Ironman:
        return UsaIronman()


if __name__ == '__main__':
    factory = RusIronmanFactory()
    rus_ironman = RusIronman()
    rus_ironman1 = factory.create()
    print(rus_ironman1 == rus_ironman)

    rus_ironman.release()
    rus_ironman1.release()

    factory = JapIronmanFactory()
    jap_ironman = factory.create()

    factory = UsaIronmanFactory()
    usa_ironman = factory.create()

    jap_ironman.release()
    usa_ironman.release()
