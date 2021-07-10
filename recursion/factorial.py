#!/user/bin/python
# -*-coding:UTF-8-*-

"""使用递归计算阶乘"""


def factorial(n: int):
    if n == 1:
        return 1
    return n * factorial(n - 1)


if __name__ == '__main__':
    number = 5
    print(factorial(number))  # 120
