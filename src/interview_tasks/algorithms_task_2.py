# Игра в кости. Делается пять бросков стандартного игрального кубика с гранями от 1 до 6 включительно.
# Делается 5 бросков (на входе в функцию подаётся массив из 5 значений кубика). Задача подсчитать количество очков,
# согласно эквивалентам по комбинациям ниже.

# Three 1's => 1000 points
# Three 6's => 600 points
# Three 5's => 500 points
# Three 4's => 400 points
# Three 3's => 300 points
# Three 2's => 200 points
# One 1 => 100 points
# One 5 => 50 points

# Учитывать, что одна цифра выступает либо в составе тройки, либо независимо. Без повторного учёта.

def play_score(arr: list) -> int:
    score = 0

    for i in range(1, 7):
        i_counter = arr.count(i)
        if i_counter >= 3:
            score += 1000 if i == 1 else i * 100
            i_counter -= 3

        score += 100 * i_counter if i == 1 else 50 * i_counter if i == 5 else 0

    return score


def main():
    assert play_score([5, 1, 3, 4, 1]) == 250
    assert play_score([1, 1, 1, 3, 1]) == 1100
    assert play_score([2, 3, 4, 6, 2]) == 0
    assert play_score([4, 4, 4, 3, 3]) == 400
    assert play_score([2, 4, 4, 5, 4]) == 450


if __name__ == '__main__':
    main()
