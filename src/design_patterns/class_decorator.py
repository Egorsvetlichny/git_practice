from abc import ABCMeta, abstractmethod


class IIronman(metaclass=ABCMeta):
    @abstractmethod
    def release_ironman(self):
        pass


class OrdinaryIronman(IIronman):
    def __init__(self, model):
        self._model = model

    def release_ironman(self):
        print(f'Выпущен железный человек модели {self._model}!')


class UpgradeIronman(IIronman):
    def __init__(self, ironman: IIronman):
        self._ironman = ironman

    @abstractmethod
    def release_ironman(self):
        self._ironman.release_ironman()


class FrozenShieldIronman(UpgradeIronman):
    def __init__(self, ironman: IIronman):
        super().__init__(ironman)

    def release_ironman(self):
        print("Покрытие деталей железного человека защитой от холода.")
        self._ironman.release_ironman()
        print("Железный человек имеет устойчивость к сверхнизким температурам.")


class LaserExtraWeaponIronman(UpgradeIronman):
    def __init__(self, ironman: IIronman):
        super().__init__(ironman)

    def release_ironman(self):
        print("Установка лазера в спинной отдел железного человека.")
        self._ironman.release_ironman()
        print("Железный человек обладает встроенным лазером в качестве дополнительного оружия")


class MissileShieldIronman(UpgradeIronman):
    def __init__(self, ironman: IIronman):
        super().__init__(ironman)

    def release_ironman(self):
        print("Установка систем ПВО в корпус железного человека.")
        self._ironman.release_ironman()
        print("Железный человек имеет системы ПВО для сбития вражеских ракет.")


if __name__ == '__main__':
    first_ironman = OrdinaryIronman('c-150M')
    first_ironman.release_ironman()

    print()

    frozen_sh_ironman = FrozenShieldIronman(first_ironman)
    frozen_sh_ironman.release_ironman()

    print()

    miss_sh_ironman = MissileShieldIronman(frozen_sh_ironman)
    miss_sh_ironman.release_ironman()

    print()

    second_ironman = OrdinaryIronman('KrW-20JI')

    lazer_extra_ironman = LaserExtraWeaponIronman(FrozenShieldIronman(second_ironman))
    lazer_extra_ironman.release_ironman()
