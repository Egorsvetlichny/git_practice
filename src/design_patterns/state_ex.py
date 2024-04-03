from abc import ABCMeta, abstractmethod


class IState(metaclass=ABCMeta):
    def __init__(self):
        self._blender: 'Blender' = None

    @abstractmethod
    def next_state(self):
        pass

    @abstractmethod
    def previous_state(self):
        pass


class Blender:
    def __init__(self, state: IState):
        self.set_state(state)

    def set_state(self, state):
        self.__state = state
        self.__state._blender = self

    def next_state(self):
        self.__state.next_state()

    def previous_state(self):
        self.__state.previous_state()


class FirstState(IState):
    def next_state(self):
        print('Переключение из первого состояния во второе')
        self._blender.set_state(SecondState())

    def previous_state(self):
        print('Первое состояние')


class SecondState(IState):
    def next_state(self):
        print('Переключение из второго состояния в третье')
        self._blender.set_state(ThirdState())

    def previous_state(self):
        print('Переключение из второго состояния в первое')
        self._blender.set_state(FirstState())


class ThirdState(IState):
    def next_state(self):
        print('Третье состояние')

    def previous_state(self):
        print('Переключение из третего состояния во второе')
        self._blender.set_state(SecondState())


if __name__ == '__main__':
    blender = Blender(FirstState())

    blender.previous_state()

    blender.next_state()
    blender.next_state()
    blender.next_state()

    blender.previous_state()
    blender.previous_state()
    blender.previous_state()
