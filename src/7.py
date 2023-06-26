#!/usr/bin/env python3
#-*- coding: utf-8 -*-
#
#      Copyright:  (C) 2023 shachi All rights reserved.
#
#           File: .\src\7.py
#         Author: shachi <shachi1758@outlook.com>
#    Description: 2023-06-25.md
#

def main():
    # * 使用 dict
    d: dict[str, int] = {"nike": 1, "mike": 2, "jack": 3}
    print(d["nike"])
    d1: dict[str, str] = dict(mike = "boy", jack = "boy", dora = "girl")
    print(d1)
    # 通过 key 获取 value
    d["Dora"] = 5
    print(d["Dora"])
    # 判断 key 是否存在
    if "nike" in d:
        print("%s is exists!" % "Nike")
    # 使用 get() 方法获取 value
    print(d.get("Mike", 1))
    # 删除键值对
    d.pop("mike")
    print(d.get("mike"))

    # * 使用 set
    s: set[int] = set([1,2,3])
    print(s)
    s1: set[int] = {1,2,3,4}
    print(s1)
    # 使用 add() 方法添加元素。
    s.add(1)
    s.add(4)
    print(s)
    s.remove(1)
    print(s)
    # 交集、并集等操作。
    print("---")
    print(s & s1)
    print(s | s1)

if __name__ == '__main__':
    main()
