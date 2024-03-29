from abc import ABCMeta, abstractmethod


class IItem(metaclass=ABCMeta):
    def __init__(self, name):
        self._name = name
        self._owner_name = None

    def set_owner(self, owner):
        self._owner_name = owner

    @abstractmethod
    def add(self, sub_item):
        pass

    @abstractmethod
    def remove(self, sub_item):
        pass

    @abstractmethod
    def display(self):
        pass


class ClickableItem(IItem):
    def __init__(self, name):
        super().__init__(name)

    def add(self, sub_item):
        raise Exception('У кликабельного элемента не может быть подэлемент')

    def remove(self, sub_item):
        raise Exception('У кликабельного элемента не может быть подэлемент')

    def display(self):
        print(self._owner_name + self._name)


class DropDownItem(IItem):
    def __init__(self, name):
        super().__init__(name)
        self.__sub_menu = []

    def add(self, sub_item: IItem):
        sub_item.set_owner(self._name)
        self.__sub_menu.append(sub_item)

    def remove(self, sub_item: IItem):
        self.__sub_menu.remove(sub_item)

    def display(self):
        for item in self.__sub_menu:
            if self._owner_name is not None:
                print(self._owner_name, end='')
            item.display()


if __name__ == '__main__':
    file = DropDownItem('Файл->')

    create = DropDownItem('Создать->')
    open_ = DropDownItem('Открыть->')
    exit_ = ClickableItem('Выход->')

    file.add(create)
    file.add(open_)
    file.add(exit_)

    project = ClickableItem('Проект->')
    repo = ClickableItem('Репозиторий->')
    directory = ClickableItem('Директория->')

    create.add(project)
    create.add(repo)
    create.add(directory)

    folder = ClickableItem('Папка->')
    archive = ClickableItem('Архив->')
    doc = ClickableItem('Документ->')


    open_.add(folder)
    open_.add(archive)
    open_.add(doc)

    file.display()

    print()

    file.remove(open_)

    file.display()

    print()

    file.remove(create)

    file.display()
