#!/usr/bin/env python3
#-*- coding: utf-8 -*-
#
#      Copyright:  (C) 2023 shachi All rights reserved.
#
#           File: .\src\6.py
#         Author: shachi <shachi1758@outlook.com>
#    Description: 循环
#

def main():
    nums: list[int] = [1,3,4,5]
    for num in nums:
        print(num)
    for num in range(10):
        print(num)

    count: int = 0
    sum: int = 0
    while count <=100:
        sum += count
        count += 1
    print(sum)

    count = 0
    sum = 0
    while True:
        sum += count
        count += 1
        if count > 100:
            break
    print(sum)

    count = 0
    sum = 0
    while True:
        count += 1
        if (count % 2 != 0):
            continue
        sum += count
        if count >= 100:
            break
    print(sum)


if __name__ == '__main__':
    main()
