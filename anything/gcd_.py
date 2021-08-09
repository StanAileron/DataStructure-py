#!/user/bin/python
# -*-coding:UTF-8-*-

"""求两个自然数的最大公约数"""
from typing import Tuple


def gcd_by_euclid(a: int, b: int) -> int:
    """使用欧几里得算法求最大公约数"""
    if b == 0:
        return a
    elif a < b:
        return gcd_by_euclid(b, a)
    else:
        return gcd_by_euclid(a - b, b)


def gcd(a: int, b: int) -> int:
    """使用模运算改进上述算法"""
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def ext_gcd(x: int, y: int) -> Tuple[int, int, int]:
    if y == 0:
        return x, 1, 0

    else:
        d, a, b = ext_gcd(y, x % y)
        return d, b, a - (x // y) * b


if __name__ == '__main__':
    print(gcd_by_euclid(32, 240))  # 16

    print(gcd(32, 240))  # 16
