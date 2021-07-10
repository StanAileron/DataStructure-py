#!/user/bin/python
# -*-coding:UTF-8-*-


"""将数字转换为字符串"""

numbers = "0123456789"


def int_to_str(number: int) -> str:
    if number < 10:
        return numbers[number]

    return int_to_str(number // 10) + numbers[number % 10]


if __name__ == '__main__':
    num = 9832
    print(int_to_str(num))  # 9832
