from abc import ABCMeta


class Ironman:
    def __init__(self):
        self.__character = ''

    def get_character(self):
        return self.__character

    def add_character(self, new_character):
        self.__character += new_character


class IIronmanCreator(metaclass=ABCMeta):
    def create_body(self):
        pass

    def create_head(self):
        pass

    def create_legs(self):
        pass

    def create_arms(self):
        pass

    def create_weapon(self):
        pass

    def get_ironman(self) -> Ironman:
        pass


class IronmanModel1Creator(IIronmanCreator):
    def __init__(self):
        self.__ironman = Ironman()

    def create_body(self):
        self.__ironman.add_character("Произведён корпус железного человека модели 1;\n")

    def create_head(self):
        self.__ironman.add_character("Добавлена голова железного человека модели 1;\n")

    def create_legs(self):
        self.__ironman.add_character("Произведены ноги железного человека модели 1;\n")

    def create_arms(self):
        self.__ironman.add_character("Созданы руки железного человека модели 1;\n")

    def create_weapon(self):
        self.__ironman.add_character("Добавлено оружие для железного человека модели 1;\n")

    def get_ironman(self) -> Ironman:
        return self.__ironman


class IronmanModel2Creator(IIronmanCreator):
    def __init__(self):
        self.__ironman = Ironman()

    def create_body(self):
        self.__ironman.add_character("Произведён корпус железного человека модели 2;\n")

    def create_head(self):
        self.__ironman.add_character("Добавлена голова железного человека модели 2;\n")

    def create_legs(self):
        self.__ironman.add_character("Произведены ноги железного человека модели 2;\n")

    def create_arms(self):
        self.__ironman.add_character("Созданы руки железного человека модели 2;\n")

    def create_weapon(self):
        self.__ironman.add_character("Добавлено оружие для железного человека модели 2;\n")

    def get_ironman(self) -> Ironman:
        return self.__ironman


class Director:
    def __init__(self, ironman_creator: IIronmanCreator):
        self.__ironman_creator = ironman_creator

    def set_ironman_creator(self, ironman_creator: IIronmanCreator):
        self.__ironman_creator = ironman_creator

    def produce_full_ironman(self) -> Ironman:
        self.__ironman_creator.create_body()
        self.__ironman_creator.create_head()
        self.__ironman_creator.create_arms()
        self.__ironman_creator.create_legs()
        self.__ironman_creator.create_weapon()
        return self.__ironman_creator.get_ironman()

    def produce_body_and_head_ironman(self) -> Ironman:
        self.__ironman_creator.create_head()
        self.__ironman_creator.create_body()
        return self.__ironman_creator.get_ironman()

    def produce_weapon_ironman(self) -> Ironman:
        self.__ironman_creator.create_weapon()
        return self.__ironman_creator.get_ironman()


if __name__ == '__main__':
    # Полная сборка железного человека модели 1
    ironman_model1_creator = IronmanModel1Creator()
    director = Director(ironman_model1_creator)
    ironman_model1 = director.produce_full_ironman()
    print(ironman_model1.get_character())

    # Частичная сборка железного человека модели 2 (Голова и туловище)
    ironman_model2_creator = IronmanModel2Creator()
    director.set_ironman_creator(ironman_model2_creator)
    ironman_model2 = director.produce_body_and_head_ironman()
    print(ironman_model2.get_character())

    # Частичная сборка железного человека модели 1 (Только оружие)
    ironman_model1_creator = IronmanModel1Creator()
    director.set_ironman_creator(ironman_model1_creator)
    ironman_model1 = director.produce_weapon_ironman()
    print(ironman_model1.get_character())
