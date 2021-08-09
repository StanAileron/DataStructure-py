#!/user/bin/python
# -*-coding:UTF-8-*-

"""求 x^n mod p的余数:
- 同余定理：
    1. 若 a mod p = b mo d p，则 (a + c) mod p = (b + c) mod p；
    2. 若 a mod p = b mo d p，则 ac mod p = bc mod p；
    3. 若 a mod p = b mo d p，则 a ^ n mod p = b ^ n mod p；

- 运用第三条同余定理即可不用在算出x^n的大小的情况下，求得x^n的余数。
"""


def mod_exp(x: int, n: int, p: int) -> int:
    result = 1
    while n > 0:
        result = result * x
        result = result % p
        n -= 1

    return result


def mod_exp_by_recursion(x: int, n: int, p: int) -> int:
    """x ^ n 的递归定义：
        - (x * x) ^ (n // 2)，n 为偶数
        - (x * x ^ (n-1)) = x * (x * x) ^ (n // 2)，n为计数
    """
    if n == 0:
        return 1

    t = (x * x) % p

    # 无论n为奇数还是偶数，都有因子(x * x) ^ (n // 2)
    tmp = mod_exp_by_recursion(t, n // 2, p)

    # 如果n为奇数，那么还有额外的因子x
    if n % 2 != 0:
        tmp = (tmp * x) % p

    return tmp


if __name__ == '__main__':
    print(mod_exp(3, 1254906, 10))  # 9

    print(mod_exp_by_recursion(3, 1254906, 10))  # 9
