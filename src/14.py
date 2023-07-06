#!/usr/bin/env python3
#-*- coding: utf-8 -*-
#
#      Copyright:  (C) 2023 shachi All rights reserved.
#
#           File: .\src\14.py
#         Author: shachi <shachi1758@outlook.com>
#    Description: 返回函数
#
from typing import Callable
def lazy_sum(*args: int) -> Callable[[],int] :
    def sum() -> int:
        ax = 0
        for n in args:
            ax: int= ax + n
        return ax
    return sum

def count() -> list[Callable[[],int]]:
    fs: list[Callable[[],int]] = []
    for i in range(1, 4):
        def f() -> int:
            return i * i
        fs.append(f)
    return fs

def my_count() -> list[Callable[[],int]]:
    def f(j)-> Callable[[],int]:
        def g()-> int:
            return j*j
        return g
    fs:list[Callable[[],int]] = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs

def inc() -> Callable[[], int]:
    x: int = 0
    def fn() -> int:
        nonlocal x
        x = x + 1
        return x
    return fn

def createCounter() -> Callable[[], int]:
    x: int = 0
    def counter() -> int:
        nonlocal x
        x += 1
        return x
    return counter


def main() -> None:
    # func: Callable[[],int] = lazy_sum(1, 3, 5, 7, 9)
    # print(func())
    func1: Callable[[], int] = createCounter()
    print(func1(), func1(), func1())
    # * lambda 函数
    L: list[int] = list(filter(lambda x: x % 2 == 1,range(1, 20)))
    print(L)

if __name__ == '__main__':
    main()