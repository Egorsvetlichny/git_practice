# Напишите программу, которая извлекает данные о моделях, конфигурации и стоимости 117-ти ноутбуков,
# и записывает полученную информацию в csv файл.


from bs4 import BeautifulSoup
import requests


def parse_laptop_info():
    url = 'https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    models = soup.find_all('a', 'title')
    models = [model['title'] for model in models]
    descriptions = soup.find_all('p', 'description card-text')
    prices = soup.find_all('h4', 'price float-end card-title pull-right')

    with open('laptop_models.csv', 'w', encoding='utf-8') as csv_file:
        csv_file.write('Model;Description;Price\n')
        for m, d, p in zip(models, descriptions, prices):
            csv_file.write(f'{m};{d.get_text()};{p.get_text()}\n')


def main():
    parse_laptop_info()


if __name__ == '__main__':
    main()
