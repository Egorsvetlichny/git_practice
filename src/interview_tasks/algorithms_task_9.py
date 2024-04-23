# Реализовать хэштег-генератор, который принимает строку, возвращает эту же строку, начинающуюся с символа #,
# не содержащую пробелов, и каждое новое слово начинается с заглавной буквы. Если исходная строка содержит более 50
# символов, верните false.

# Например: input 'hello world and everyone' - output '#HelloWorldAndEveryone'


from typing import Union


def hashtag_generator(string: str) -> Union[str, bool]:
    return '#' + ''.join(string.title().split()) if string and len(string) <= 50 else False


def main():
    assert hashtag_generator('hello world and everyone') == '#HelloWorldAndEveryone'
    assert hashtag_generator('') is False
    assert hashtag_generator('I Like yOU, buddy!') == '#ILikeYou,Buddy!'
    assert hashtag_generator('fwer werwer werwer ew ew fwerwerwe werwe wer werwerwe wrwrwwrwwrwe rwerrw') is False


if __name__ == '__main__':
    main()
