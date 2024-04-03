from abc import ABCMeta, abstractmethod


class IDataReader(metaclass=ABCMeta):
    @abstractmethod
    def read(self, data):
        pass


class DataBaseReader(IDataReader):
    def read(self, data):
        print(f'Данные, считанные из базы данных: {data}')


class FileReader(IDataReader):
    def read(self, data):
        print(f'Данные, считанные из файла:  {data}')


class TelegramDataReader(IDataReader):
    def read(self, data):
        print(f'Данные, считанные из бота в телеграмме:  {data}')


class ResourceReader:
    def __init__(self, reader: IDataReader):
        self.__reader = reader

    def set_reader(self, reader: IDataReader):
        self.__reader = reader

    def read_data(self, data):
        self.__reader.read(data)


if __name__ == '__main__':
    data = 'Data Base data'
    res_reader = ResourceReader(DataBaseReader())
    res_reader.read_data(data)

    data = 'Telegram bot data'
    res_reader.set_reader(TelegramDataReader())
    res_reader.read_data(data)

    data = 'Data from file'
    res_reader.set_reader(FileReader())
    res_reader.read_data(data)
