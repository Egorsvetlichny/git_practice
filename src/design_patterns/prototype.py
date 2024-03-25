import copy


class Ironman:
    __name = ''
    __params = {'model': 'destroyer', 'power': 80, 'weapon': 'Lazer'}

    def __init__(self, donor=None):
        if donor is not None:
            self.__name = donor.get_name()
            self.__params = copy.deepcopy(donor.get_params())

    def set_name(self, new_name):
        self.__name = new_name

    def get_name(self):
        return self.__name

    def set_power(self, new_power):
        self.__params['power'] = new_power

    def set_weapon(self, new_weapon):
        self.__params['weapon'] = new_weapon

    def get_params(self):
        return self.__params

    def clone(self):
        return Ironman(self)


if __name__ == '__main__':
    donor_ironman = Ironman()
    donor_ironman.set_name("Tony Stark")

    clone_ironman = donor_ironman.clone()

    print('Donor: ', donor_ironman.get_name(), donor_ironman.get_params())
    print('Clone: ', clone_ironman.get_name(), clone_ironman.get_params())

    clone_ironman.set_name('Monty Python')
    clone_ironman.set_weapon('Minigun')
    clone_ironman.set_power(100)

    print()

    print('Donor: ', donor_ironman.get_name(), donor_ironman.get_params())
    print('Clone: ', clone_ironman.get_name(), clone_ironman.get_params())
