# Аннотации типов в Python.
# Используется для описания типов данных.
# В данном модуле представлены популярные аннотации, которые я не встречал ранее.

from typing import List, TypeAlias, Union, Literal, Annotated, Optional

some_int_list: List[int] = [1, 2, 3, 4, 5]
some_str_list: list[str] = ["1", "2", "3", "4", "5"]

name = bool


def return_bool() -> name: pass


name: TypeAlias = str


def return_str() -> name: pass


def foo() -> Optional[int]: pass


def bar() -> Union[int, float]: pass


def baz() -> Literal["a", "b"]: pass


def qux() -> Annotated[int, "a"]: pass


def bar_now() -> int | float: pass
