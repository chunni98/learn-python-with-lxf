#
#      Copyright:  (C) 2023 shachi All rights reserved.
#
#           File: .\src\3.py
#         Author: shachi <shachi1758@outlook.com>
#    Description: 数据类型
#

def main():
    print("十进制整数:", 1, 133, -100001, 0)
    print("十六进制整数:", 0xff23edc3)
    print("数字间隔：", 1_0000_0000, 0xff23_edc3)
    print("科学计数法：", 1.23e10)
    print("浮点数运算误差：0.999 + 0.0001 == 0.1 ?", 0.9999 + 0.0001 == 0.1)
    print("转义：\"")
    print(r"不转义：\n\n\t\r\b\\")
    print(r'''
    你好！\n
    hello\n
    こんにちは\n
    안녕하세요\n
    Bonjour\n
    ''')
    print(True and True)
    print(True or False)
    print(not True)

    age = 19
    if age > 18:
        print(age, "> 18")
    b = 13
    b = '13'
    b = True
    b = None

    PI = 3.1415926535
    print(100 / 3)
    print(100 // 3)

if __name__ == '__main__':
    main()
