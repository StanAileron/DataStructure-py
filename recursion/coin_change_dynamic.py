#!/user/bin/python
# -*-coding:UTF-8-*-


"""使用动态规划解决找零问题"""
from typing import List


def coin_change(coin_list: List[int], change: int, coin_counts: List[int], coin_lst: List[int]):
    for i in range(1, change + 1):
        min_coin_counts = i  # 初始化当前金额可能需要的最大硬币数

        for j in (j for j in coin_list if j <= i):
            if coin_counts[i - j] + 1 <= min_coin_counts:  # 通过查表得出i美分减去j硬币后的金额对应的最小硬币数
                min_coin_counts = coin_counts[i - j] + 1
                coin_lst[i] = j

        coin_counts[i] = min_coin_counts

    return coin_counts[change], coin_lst


def print_coins(coin_list: List[int], change: int):
    print("Need coin: ")
    while change != 0:
        print(coin_list[change], end=" ")
        change = change - coin_list[change]
    print()


if __name__ == '__main__':
    coins, coin_lt = coin_change([1, 5, 10, 25], 63, [0] * 64, [0] * 64)
    print("Need coin counts: ", coins)
    print_coins(coin_lt, 63)
    print("Coin list: ", coin_lt)

# Need coin counts:  6
# Need coin:
# 25 25 10 1 1 1
# Coin list:  [0, 1, 1, 1, 1, 5, 5, 5, 5, 5, 10, 10, 10, 10, 10, 10, 10,
# 10, 10, 10, 10, 10, 10, 10, 10, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25,
# 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25,
# 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25]
