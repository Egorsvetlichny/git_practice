import csv


def test_writerow_csv(*args):
    with open('test_writerow.csv', 'w', encoding='cp1251', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=' ')
        for arr in args:
            writer.writerow(arr)


def test_writerows_csv(*args):
    with open('test_writerows.csv', 'w', encoding='cp1251', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=';')
        writer.writerows(args)


# def


if __name__ == '__main__':
    data = ('first_name', 'last_name')
    data1 = ['John', 'Sina']
    data2 = ['Sarah', 'Bahman']
    data3 = ['Danny', 'Robinson']

    test_writerow_csv(data, data1, data2, data3)

    test_writerows_csv(data, data1, data2, data3)
