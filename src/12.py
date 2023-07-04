#!/usr/bin/env python3
#-*- coding: utf-8 -*-
#
#      Copyright:  (C) 2023 shachi All rights reserved.
#
#           File: .\src\12.py
#         Author: shachi <shachi1758@outlook.com>
#    Description: 函数式编程
#
from typing import Callable

# * 高阶函数
def add(x: int, y: int, f:Callable[[int], int]) -> int:
    return f(x) + f(y)

def func(x: int) -> int:
    return x * x

def fn(x: int, y: int) -> int:
    return x * 10 + y

from functools import reduce

def normalize(name: str) -> str:
    return name.title()

def prod(L: list[int]) -> int:
    return reduce(lambda x, y: x * y, L)

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def char2num(s):
    return DIGITS[s]

def str2float(s: str) -> float:
    l: list[str] = s.split('.')
    print(l[0])
    print(l[1])
    f1: float = reduce(lambda x, y: x * 10 + y, map(char2num, l[0]))
    f2: float = reduce(lambda x, y: x * 10 + y, map(char2num, l[1])) / (10 ** len(l[1]))
    return f1 + f2



def main() -> None:
    add(1, 2, abs)
    # * map
    r = map(func, [1,2,3,4,5])
    print(list(r))
    print(reduce(fn,[1, 3, 5, 7, 9]))
    print(str2float("1382.345"))


if __name__ == '__main__':
    main()
