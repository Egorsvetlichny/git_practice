from abc import ABCMeta, abstractmethod


class Engine(metaclass=ABCMeta):
    @abstractmethod
    def release_engine(self):
        pass


class RusEngine(Engine):
    def release_engine(self):
        print("Russian engine")


class EngEngine(Engine):
    def release_engine(self):
        print("English engine")


class Weapon(metaclass=ABCMeta):
    @abstractmethod
    def release_weapon(self):
        pass


class PlasmaWeapon(Weapon):
    def release_weapon(self):
        print("Plasma weapon")


class LazerWeapon(Weapon):
    def release_weapon(self):
        print("Lazer weapon")


class MinigunWeapon(Weapon):
    def release_weapon(self):
        print("Minigun weapon")


class Ironman(metaclass=ABCMeta):
    @abstractmethod
    def release_ironman(self, engine: Engine, weapon: Weapon):
        pass


class RusIronman(Ironman):
    def release_ironman(self, engine: Engine, weapon: Weapon):
        print("Release Russian Ironman")
        print("He has:")
        engine.release_engine()
        weapon.release_weapon()
        print()


class EngIronman(Ironman):
    def release_ironman(self, engine: Engine, weapon: Weapon):
        print("Release English Ironman")
        print("He has:")
        engine.release_engine()
        weapon.release_weapon()
        print()


class Factory(metaclass=ABCMeta):
    @abstractmethod
    def create_engine(self) -> Engine:
        pass

    @abstractmethod
    def create_weapon(self) -> Weapon:
        pass

    @abstractmethod
    def create_ironman(self) -> Ironman:
        pass


class RusFactory(Factory):
    def create_engine(self) -> Engine:
        return RusEngine()

    def create_weapon(self) -> Weapon:
        return PlasmaWeapon()

    def create_ironman(self) -> Ironman:
        return RusIronman()


class EngFactory(Factory):
    def create_engine(self) -> Engine:
        return EngEngine()

    def create_weapon(self) -> Weapon:
        return MinigunWeapon()

    def create_ironman(self) -> Ironman:
        return EngIronman()


class RusEngFactory(Factory):
    def create_engine(self) -> Engine:
        return RusEngine()

    def create_weapon(self) -> Weapon:
        return LazerWeapon()

    def create_ironman(self) -> Ironman:
        return EngIronman()


if __name__ == '__main__':
    rus_factory = RusFactory()
    rus_engine = rus_factory.create_engine()
    plasma_weapon = rus_factory.create_weapon()
    rus_ironman = rus_factory.create_ironman()
    rus_ironman.release_ironman(rus_engine, plasma_weapon)

    eng_factory = EngFactory()
    eng_engine = eng_factory.create_engine()
    minigun_weapon = eng_factory.create_weapon()
    eng_ironman = eng_factory.create_ironman()
    eng_ironman.release_ironman(eng_engine, minigun_weapon)

    rus_eng_factory = RusEngFactory()
    engine = rus_eng_factory.create_engine()
    lazer_weapon = rus_eng_factory.create_weapon()
    ironman = rus_eng_factory.create_ironman()
    ironman.release_ironman(engine, lazer_weapon)
