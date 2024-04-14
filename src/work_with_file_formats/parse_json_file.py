import json
import random
from datetime import datetime


def load_json(file_name: str) -> dict:
    with open(file_name, 'r', encoding='utf8') as json_file:
        return json.load(json_file)


def dump_json(file_name: str, json_data: dict) -> None:
    with open(file_name, 'w', encoding='cp1251') as json_file:
        json.dump(json_data, json_file, indent=4)


if __name__ == '__main__':
    data = load_json(r'C:\Users\fkhor\PycharmProjects\git_practice\src\work_with_file_formats\test_json_file')
    print(data)

    data = data['catalogs'][1]
    data['date_end'] = datetime.now().strftime('%y-%m-%d')
    data['random_int'] = random.randint(100, 1500)
    dump_json('updated_json_file', data)
