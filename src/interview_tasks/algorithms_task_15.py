# Вам дано двоичное дерево, в котором находятся целые числа.
# Ваш скрипт должен вывести последовательность чисел, которая бы показывала, как он проходил по двоичному дереву.
#
# При этом количество попыток не должно превышать 100, количество ветвей дерева не должно быть меньше нуля и
# не должно превышать 1000, а числа дерева не должны быть отрицательными.

from sys import stdin, setrecursionlimit
from queue import Queue

setrecursionlimit(10 ** 7)


class BinaryTreeNode:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None


def get_level_order(root):
    output = []

    if root is None:
        return output

    level = Queue()
    level.put(root)

    while not level.empty():
        level_size = level.qsize()

        while level_size != 0:
            curr = level.get()
            output.append(curr.val)

            if curr.left is not None:
                level.put(curr.left)

            if curr.right is not None:
                level.put(curr.right)

            level_size = level_size - 1

    return output


def take_input():
    arr = list(map(int, stdin.readline().strip().split(" ")))

    root_data = arr[0]

    n = len(arr)

    if root_data == -1:
        return None

    root = BinaryTreeNode(root_data)
    q = Queue()
    q.put(root)
    index = 1
    while q.qsize() > 0:
        current_node = q.get()
        left_child = arr[index]

        if left_child != -1:
            left_node = BinaryTreeNode(left_child)
            current_node.left = left_node
            q.put(left_node)

        index += 1
        right_child = arr[index]

        if right_child != -1:
            right_node = BinaryTreeNode(right_child)
            current_node.right = right_node
            q.put(right_node)

        index += 1

    return root


def print_ans(ans):
    for x in ans:
        print(x, end=" ")
    print()


def main():
    tree = int(stdin.readline().strip())
    for i in range(tree):
        root = take_input()
        ans = get_level_order(root)
        print_ans(ans)


if __name__ == '__main__':
    main()
