from abc import ABCMeta, abstractmethod


class IVisitor(metaclass=ABCMeta):
    @abstractmethod
    def visit(self, place: 'IPlace'):
        pass


class IPlace(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor: IVisitor):
        pass


class TravelPlace(IPlace):
    def accept(self, visitor: IVisitor):
        visitor.visit(self)


class CinemaPlace(IPlace):
    def accept(self, visitor: IVisitor):
        visitor.visit(self)


class CafePlace(IPlace):
    def accept(self, visitor: IVisitor):
        visitor.visit(self)


class TheaterPlace(IPlace):
    def accept(self, visitor: IVisitor):
        visitor.visit(self)


class WeekendMaker(IVisitor):
    def __init__(self):
        self.case = ''

    def visit(self, place: 'IPlace'):
        if isinstance(place, CinemaPlace):
            self.case = 'Поход в кинотеатр'
        elif isinstance(place, CafePlace):
            self.case = 'Поход в кафе'
        elif isinstance(place, TravelPlace):
            self.case = 'Путешествие'
        else:
            self.case = 'Поход в неизвестное место'


if __name__ == '__main__':
    cafe_place = CafePlace()
    visitor_ = WeekendMaker()
    cafe_place.accept(visitor_)
    print(visitor_.case)

    print()

    visitor_ = WeekendMaker()
    places = [CinemaPlace(), CafePlace(), TravelPlace(), TheaterPlace()]
    for place_ in places:
        place_.accept(visitor_)
        print(visitor_.case)
