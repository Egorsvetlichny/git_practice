# Есть направления пути "North", "East", "South", "West".
# Написать функцию, принимающую на вход массив строк и сокращающую все противоположные направления

# Например: Input(["North", "South", "South", "West", "East", "North", "West"]) - Output(["West"])


def reduce_direction(arr: list) -> list:
    flag = True

    while flag:
        i = counter = 0

        while i < len(arr) - 1:
            if (arr[i].lower() == 'north' and arr[i + 1].lower() == 'south') or (
                    arr[i].lower() == 'south' and arr[i + 1].lower() == 'north') or (
                    arr[i].lower() == 'west' and arr[i + 1].lower() == 'east') or (
                    arr[i].lower() == 'east' and arr[i + 1].lower() == 'west'):
                del arr[i:i + 2]
                counter += 1
            else:
                i += 1

        if counter == 0:
            return arr


def optimal_reduce_direction(arr: list) -> list:
    direction = {'north': 'south', 'south': 'north', 'west': 'east', 'east': 'west'}
    for i in range(len(arr) - 1):
        if arr[i].lower() == direction[arr[i + 1].lower()]:
            del arr[i:i + 2]
            return optimal_reduce_direction(arr)
    return arr


def main():
    assert optimal_reduce_direction(["North", "South", "South", "West", "East", "North", "West"]) == ['West']
    assert optimal_reduce_direction(['North', 'WEST', 'East', 'SOUTH']) == []
    assert optimal_reduce_direction([]) == []
    assert optimal_reduce_direction(['South']) == ['South']
    assert optimal_reduce_direction(['South', 'West', 'North', 'EAST']) == ['South', 'West', 'North', 'EAST']


if __name__ == '__main__':
    main()
