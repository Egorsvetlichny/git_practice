import csv
import json


def create_csv_title(file_name: str) -> None:
    with open(file_name, 'w', encoding='cp1251', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=';')
        writer.writerow(['Цена', 'Количество монет', 'Итоговая стоимость'])


def read_json_data(file_name: str) -> dict:
    with open(file_name) as json_file:
        data_dict = json.load(json_file)

    return data_dict


def get_needed_list_from_dict(json_data: dict) -> list:
    return json_data['data']['xrp_usd']['asks']


def write_cryptodata_to_csv(file_name: str, data: list) -> None:
    with open(file_name, 'a', encoding='cp1251', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=';')
        for item in data:
            price = item[0]
            count = item[1]
            total = price * count

            writer.writerow([price, count, total])


if __name__ == '__main__':
    csv_file_name = 'crypto_data.csv'
    json_file_name = 'crypto_data.txt'

    create_csv_title(csv_file_name)
    json_data = read_json_data(json_file_name)
    data_list = get_needed_list_from_dict(json_data)
    write_cryptodata_to_csv(csv_file_name, data_list)
