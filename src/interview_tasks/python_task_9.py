# Написать функцию, которая принимает строку и перемещает первую букву каждого слова в конец (с сохранением регистра),
# а затем добавляет "ay" в конец каждого слова. Знаки препинания оставить нетронутыми

# Например: Input('Hello, world!'), Output('elloHay, orldway!')


import string


def change_string(input_str: str) -> str:
    result = []

    for word in input_str.split():
        if not all(char in string.punctuation for char in word):
            if not word[-1].isalpha():
                alphas = ''.join([char for char in word if char.isalpha()])
                punctuation = ''.join([char for char in word if char not in alphas])
                result.append(alphas[1:] + alphas[0] + 'ay' + punctuation)
            else:
                result.append(word[1:] + word[0] + 'ay')
        else:
            result.append(word)

    return ' '.join(result)


def main():
    assert change_string('Hello,- world !?!., ...') == 'elloHay,- orldway !?!., ...'
    assert change_string('Pig latin is cool') == 'igPay atinlay siay oolcay'
    assert change_string('') == ''
    assert change_string(',./') == ',./'
    assert change_string('I') == 'Iay'
    assert change_string('E, e') == 'Eay, eay'


if __name__ == '__main__':
    main()
