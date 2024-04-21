# Напишите функцию, которая принимает url-адрес и возвращает доменное имя

def get_domain_from_url(string: str) -> str:
    string = string.replace('http://', '').replace('https://', '').replace('www.', '')
    return string.split('.')[0]


def main():
    assert get_domain_from_url('http://github.com/carbonfive/raygun') == 'github'
    assert get_domain_from_url('') == ''
    assert get_domain_from_url(' ') == ' '
    assert get_domain_from_url('http://www.zombie-bites.com') == 'zombie-bites'
    assert get_domain_from_url('https://www.cnet.com') == 'cnet'


if __name__ == '__main__':
    main()
