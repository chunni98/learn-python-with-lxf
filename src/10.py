#!/usr/bin/env python3
#-*- coding: utf-8 -*-
#
#      Copyright:  (C) 2023 shachi All rights reserved.
#
#           File: .\src\10.py
#         Author: shachi <shachi1758@outlook.com>
#    Description: This file
#

def findMinAndMax(L: list[int | float]) -> tuple[int | float | None, int | float | None]:
    if L == []:
        return (None, None)
    min: int | float = L[0]
    max: int | float = L[0]
    for val in L:
        if min > val:
            min = val
        if max < val:
            max = val
    return (min, max)


def main() -> None:
    d: dict[str, int] = {'a': 1, 'b': 2, 'c': 3}
    for key, val in d.items():
        print(key, val)

    for ch in "ABCD":
        print(ch)

    for x, y in [(1,1), (1,4), (3,5)]:
        print(x,y)

    if findMinAndMax([]) != (None, None):
        print('测试失败!')
    elif findMinAndMax([7]) != (7, 7):
        print('测试失败!')
    elif findMinAndMax([7, 1]) != (1, 7):
        print('测试失败!')
    elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
        print('测试失败!')
    else:
        print('测试成功!')

if __name__ == '__main__':
    main()
