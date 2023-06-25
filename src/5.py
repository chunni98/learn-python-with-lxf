#!/usr/bin/env python3
#-*- coding: utf-8 -*-
#
#      Copyright:  (C) 2023 shachi All rights reserved.
#
#           File: .\src\5.py
#         Author: shachi <shachi1758@outlook.com>
#    Description: This file
#

def main():
    # 列表创建
    names: list[int] = ["廖雪峰", "阮一峰", "陈皓"]
    print(names)

    # 列表长度
    print(len(names))
    # 索引访问
    print(names[0])
    print(names[-1])
    # 插入元素
    names.append("王垠")
    print(names)
    names.insert(3, "韦一笑")
    print(names)
    print(names.pop(4))

if __name__ == '__main__':
    main()
