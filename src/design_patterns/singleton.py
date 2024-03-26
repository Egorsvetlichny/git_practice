class DataBaseConnection:
    __db_connection = None

    def __new__(cls, *args, **kwargs):
        if cls.__db_connection is None:
            cls.__db_connection = object.__new__(cls)
            print("Connection to DataBase")
        return cls.__db_connection

    def select_data(self):
        return self.__data

    def insert_data(self, new_data):
        self.__data = new_data


if __name__ == '__main__':
    connection = DataBaseConnection()
    connection.insert_data('text')
    print(f"Параметр первого объекта: {connection.select_data()}")

    try_new_connection = DataBaseConnection()
    # Специально не присваиваем новому объекту никаких данных
    print(f"Параметр второго объекта: {try_new_connection.select_data()}")

    print(try_new_connection is connection)
