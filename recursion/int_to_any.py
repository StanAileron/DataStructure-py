#!/user/bin/python
# -*-coding:UTF-8-*-


"""将是十进制数字转换为任意进制的字符串"""

nums = "0123456789ABCDEF"


def int_to_any(number: int, base: int) -> str:
    if number < base:
        return nums[number]
    return int_to_any(number // base, base) + nums[number % base]


if __name__ == '__main__':
    n = 1231239
    print(int_to_any(n, 2))  # 100101100100110000111
    print(int_to_any(n, 8))  # 4544607
    print(int_to_any(n, 16))  # 12C987
