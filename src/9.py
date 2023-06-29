#!/usr/bin/env python3
#-*- coding: utf-8 -*-
#
#      Copyright:  (C) 2023 shachi All rights reserved.
#
#           File: .\src\9.py
#         Author: shachi <shachi1758@outlook.com>
#    Description: This file
#
def trim(s: str) -> str:
    i: int = 0
    while True:
        if s[i] != ' ':
            break
        i += 1
    s = s[i:]
    i = 0
    while True:
        if s[i] == ' ':
            break
        i += 1
    s = s[:i]
    return s



def main() -> None:
    # * 切片
    l1: list[str] = ["Mike", "Jack", "Jason", "Karl", "Dora"]
    print(l1[0:3])
    print(l1[:3])
    print(l1[1:3])
    print(l1[-2:])
    print(l1[-2:-1])
    L: list[int] = list(range(100))
    print(L[10:20])
    # 倒数第 20 个数到倒数第 11 个数，每两个数取一个。
    print(L[-20:-10:2])
    # 复制一个 list
    print(L[:])
    # tuple
    print((0,1,3,4,5,6)[2:])
    s: str = "   hello   "
    print(len(s))
    s = trim(s)
    print(s)
    print(len(s))


if __name__ == '__main__':
    main()
