#!/usr/bin/env python3
#-*- coding: utf-8 -*-
#
#      Copyright:  (C) 2023 shachi All rights reserved.
#
#           File: .\src\13.py
#         Author: shachi <shachi1758@outlook.com>
#    Description: filter、sorted
#

def is_odd(num: int) -> bool:
    if num % 2 == 1:
        return True
    else:
        return False

def is_palindrome(n: int) -> bool:
    return str(n) == str(n)[::-1]

# * sorted
def by_name(t: tuple[str, int]) -> str:
    return t[0]

# 按成绩从高到低排序。
def by_score(t: tuple[str, int]) -> int:
    return -t[1]

from typing import Iterator
def main() -> None:
    # * filter
    l: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    k: Iterator = filter(is_odd, l)
    print(list(k))
    L: list[tuple[str, int]] = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
    L2: list[tuple[str, int]]  = sorted(L, key=by_name)
    print("L2:", L2)
if __name__ == '__main__':
    main()
