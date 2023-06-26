#!/usr/bin/env python3
#-*- coding: utf-8 -*-
#
#      Copyright:  (C) 2023 shachi All rights reserved.
#
#           File: .\src\8.py
#         Author: shachi <shachi1758@outlook.com>
#    Description: This file
#

# * 函数定义
def func(x: int) -> int:
    if x > 0:
        return x
    else:
        return -x

# 空函数
def nop() -> None:
    pass

import math
# 返回多个值的函数
def func2(x: int, y: int, step: int, angle: float = 0) -> tuple[float, float]:
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return (nx, ny)

def quadratic(a: int, b: int, c: int) -> tuple[float, float]:
    x1 = -b + math.sqrt(b ** 2 - 4 * a * c)
    x2 = -b - math.sqrt(b ** 2 - 4 * a * c)
    y = 2 * a

    return (x1 / y, x2 / y)

def func3(x: int, n: int = 2) -> int:
    return x ** n

def func4(x: int, y: int, z: int = 3) -> int:
    return x + y + z

def calc(numbers: tuple[int, ...]) -> int:
    sum = 0
    for n in numbers:
        sum: int = sum + n * n
    return sum

def ttt(num: list[int]) -> None:
    num.append(2)
    return None

def calc2(*numbers: int) -> int:
    sum: int = 0
    for i in numbers:
        sum = sum + i * i
    return sum

from typing import Union
def test(**kwargs: Union[str, int]) -> None:
    pass

def test2(a: int | float | str) -> int | float | str:
    return 1

# 关键字参数
def person(name: str, age: int, **kwargs: str|int) -> None:
    print("name:", name, "age:", age, "other:", kwargs)

def mul(*args: int | float) -> int | float:
    ans: int | float = 1
    for num in args:
        ans *= num
    return ans



#from typing import NoReturn
def main() -> None:
    # 使用 hex() 函数
    a: int = 17
    print(a)
    print(hex(a))
    a = 1000
    print(str(hex(a)))
    #print(func(-3))
    nop()
    print(quadratic(2, 3, 1))
    print(func3(2))
    print(func4(y = 2, x = 1))
    calc((1,3))
    ttt([3,3])
    person("张三", 2)
    person("张三", 2, gender = "man")
    person("张三", 2, gender = "man", job = "Engineer")
    extra: dict[str, str] = {"gender":"man","job":"Engineer"}
    person("李四",3,**extra)
    print(mul(3, 2.5, 7, 23))
    #while True:
        #pass

if __name__ == '__main__':
    main()
