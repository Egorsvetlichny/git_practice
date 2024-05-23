# Напишите программу для определения 10 слов, которые чаще всего встречаются в тексте сказки «Колобок»
# (без учета регистра). Предлоги учитывать не нужно.


from bs4 import BeautifulSoup
from collections import Counter
import requests


def highest_freq_words():
    url = 'https://azku.ru/russkie-narodnie-skazki/kolobok.html'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    text_tale = soup.find('div', 'entry-content')
    text_tale = text_tale.find_all('p')
    text_tale = [paragraph.get_text() for paragraph in text_tale]
    string_tale = ' '.join(text_tale)
    to_delete = '.,:;!?—'
    string_tale = ''.join([char if char not in to_delete else ' ' for char in string_tale])
    words_list = [word for word in string_tale.lower().split() if len(word) > 3]

    return Counter(words_list).most_common(10)


def main():
    for word, frequency in highest_freq_words():
        print(f'{word} - {frequency}')


if __name__ == '__main__':
    main()
