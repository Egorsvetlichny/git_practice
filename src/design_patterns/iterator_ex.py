import copy


class Stack:
    def __init__(self, stack: 'Stack' = None):
        self.__arr = [i for i in range(10)]
        self.__length = 10
        if stack is not None:
            self.__length = stack.__length
            self.__arr = copy.deepcopy(self.__arr)

    @property
    def length(self):
        return self.__length

    @property
    def arr(self):
        return self.__arr

    def pop(self):
        self.__length -= 1
        return self.__arr[self.__length]

    def __eq__(self, other):
        it1, it2 = StackIterator(self), StackIterator(other)

        while not it1.is_end() and not it2.is_end():
            if next(it1) != next(it2):
                break

        return it1.is_end() and it2.is_end()


class StackIterator:
    def __init__(self, stack: Stack):
        self.__stack = stack
        self.__index = 0

    def __iter__(self):
        return self

    def __next__(self):
        cur_index = self.__index
        self.__index += 1

        if cur_index < self.__stack.length:
            return self.__stack.arr[cur_index]
        else:
            print(f"-----Достигнут конец итератора {self}!-----")
            return 0

    def is_end(self):
        return self.__index == self.__stack.length + 1


if __name__ == '__main__':
    stack1 = Stack()
    stack2 = Stack(stack1)

    print(stack1 == stack2)

    stack1.pop()

    print(stack1 == stack2)

    stack2.pop()

    print(stack1 == stack2)
