# Напишите регулярное выражение для валидации пароля.
# Надежный пароль имеет длину от 8 до 20 символов и включает в себя хотя бы:
# - один символ в верхнем регистре;
# - один символ в нижнем регистре;
# - одну цифру;
# - один спецсимвол из набора @$!%*#?&.

import re


def password_validation(password: str) -> str:
    if re.match(r'^(?=.*\d)(?=.*[A-Z])(?=.*[a-z])(?=.*[@$!%*#?&])[\w@$!%*#?&]{8,20}$', password):
        return f'Пароль: {password} - надёжный!'
    return f'Пароль: {password} - не надёжный!'


def main():
    passwords = ['cheBur@sh!ka', 'cheBur@sh#ka5', 'Egor4@', 'Egoooooooooooooooooooor4@', '4234few!@', 'BBSDFRE47!',
                 'fewrwVSWDFRW!!!', 'fewrewFERWERF421', 'Egor_pomidoor007!']

    [print(password_validation(psw)) for psw in passwords]


if __name__ == '__main__':
    main()
