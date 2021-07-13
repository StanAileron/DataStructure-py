#!/user/bin/python
# -*-coding:UTF-8-*-


"""硬币找零问题
问题描述：给定找零金额和一组面值固定且数量不限的硬币，找出使得硬币总金额刚好等于找零金额的最小硬币数量。
"""

from typing import List


def coins_change(coin_lst: List[int], change: int) -> int:
    min_coins = change
    if change in coin_lst:
        return 1

    for coin in (coin for coin in coin_lst if coin < change):
        cur_coins = 1 + coins_change(coin_lst, change-coin)
        if cur_coins < min_coins:
            min_coins = cur_coins

    return min_coins


if __name__ == '__main__':
    print(coins_change([1, 5, 10, 25], 63))     # 6
