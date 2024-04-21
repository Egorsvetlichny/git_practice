# Напишите функцию, которая принимает url-адрес и возвращает доменное имя

def first_nonrepeat_char(string: str) -> str:
    string = string.replace('http://', '').replace('https://', '').replace('www.', '')
    return string.split('.')[0]


def main():
    assert first_nonrepeat_char('http://github.com/carbonfive/raygun') == 'github'
    assert first_nonrepeat_char('') == ''
    assert first_nonrepeat_char(' ') == ' '
    assert first_nonrepeat_char('http://www.zombie-bites.com') == 'zombie-bites'
    assert first_nonrepeat_char('https://www.cnet.com') == 'cnet'


if __name__ == '__main__':
    main()
