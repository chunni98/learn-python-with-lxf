#!/usr/bin/env python3
#-*- coding: utf-8 -*-
#
#      Copyright:  (C) 2023 shachi All rights reserved.
#
#           File: .\src\11.py
#         Author: shachi <shachi1758@outlook.com>
#    Description: 列表生成式
#

# 生成器
from typing import Iterator

def fib(max: int) -> Iterator:
    n: int = 0
    a: int = 0
    b: int = 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1

# 练习

def triangles() -> Iterator:
    l: list[int] = [1,]
    while True:
        yield l
        l = [1,] + [l[i] + l[i + 1] for i in range(len(l) - 1)] + [1,]

def main() -> None:
    # 列表生成式
    print([x * x for x in range(1, 10)])
    print([x * x for x in range(1, 10) if x % 2 == 0])
    print([m + n for m in "ABC" for n in "XYZ"])
    print([x if x % 2 == 0 else -x for x in range(1, 11)])
    # 练习

    L1 = ['Hello', 'World', 18, 'Apple', None]
    L2 = [ch.lower() for ch in L1 if isinstance(ch, str)]
    print(L2)

    ## 生成式
    g = (x * x for x in range(1, 11))
    for x in g:
        print(x)

    f = fib(6)
    for i in f:
        print(i)

    j: int = 0
    for i in triangles():
        print(i)
        j = j + 1
        if j == 10:
            break


if __name__ == '__main__':
    main()
