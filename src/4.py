#
#      Copyright:  (C) 2023 shachi All rights reserved.
#
#           File: .\src\4.py
#         Author: shachi <shachi1758@outlook.com>
#    Description: 字符串与编码
#

def main():
    print("包含中文的字符串")
    print(ord('花'))
    print(chr(66))
    print('ABC'.encode('ascii'))
    print('花'.encode('utf-8'))
    print(b'\xe8\x8a\xb1'.decode("utf-8"))
    print(b'ABC'.decode("ascii"))
    print(b'\xe8\x8a\xb1\xb3'.decode("utf-8", errors = "ignore"))
    print(len("花朵".encode("utf-8")))
    print(len("abcd"))
    print("%s" % "hello, world")
    print("my age is %02d, PI is %.2f" % (3, 3.1415926535))
    print("my age is %s, PI is %s" % (3, 3.1415926535))
    print("rate is %d%%" % 7)
    print("rate is {0}%, {1:.1f}".format(7, 12.2222))
    r= 2.5
    s = 3.14 * 4 ** 2
    print(f"面积是：{s:.2f}")


if __name__ == '__main__':
    main()
