from abc import ABCMeta, abstractmethod


class IDataReader(metaclass=ABCMeta):
    @abstractmethod
    def read_data(self):
        pass


class DataBaseReader(IDataReader):
    def read_data(self):
        print("Данные из базы данных.", end=' ')


class FileFixtureReader(IDataReader):
    def read_data(self):
        print("Данные из файла-фикстуры.", end=' ')


class IDataSender(metaclass=ABCMeta):
    def __init__(self, reader: IDataReader):
        self.reader = reader

    def set_data_reader(self, reader: IDataReader):
        self.reader = reader

    @abstractmethod
    def send(self):
        pass


class TelegramSender(IDataSender):
    def __init__(self, reader: IDataReader):
        super().__init__(reader)

    def send(self):
        self.reader.read_data()
        print("Отправлены при помощи Telegram")


class EmailSender(IDataSender):
    def __init__(self, reader: IDataReader):
        super().__init__(reader)

    def send(self):
        self.reader.read_data()
        print("Отправлены при помощи Email")


class FaxSender(IDataSender):
    def __init__(self, reader: IDataReader):
        super().__init__(reader)

    def send(self):
        self.reader.read_data()
        print("Отправлены по факсу")


if __name__ == '__main__':
    data_reader = DataBaseReader()
    sender = EmailSender(data_reader)
    sender.send()

    data_reader = FileFixtureReader()
    sender.set_data_reader(data_reader)
    sender.send()

    sender = TelegramSender(data_reader)
    sender.send()

    sender = FaxSender(DataBaseReader())
    sender.send()
