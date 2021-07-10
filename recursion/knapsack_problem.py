#!/user/bin/python
# -*-coding:UTF-8-*-


"""简单背包问题：
问题描述：一个背包里可放入重量为weight的物品，现有n件物品的集合s，其中物品的重量分别为w0、w1、、、wn-1，
        问能否从中选出若干件物品，其重量之和正好等于weight，若存在则说明此背包问题有解。

此问题可以转化为knap(weight,n)是否有解，其中n表示n件物品。
现在可分为两种情况：
    1.若knap(weight,n-1)即不考虑第n件物品有解，那么kanp(weight,n)就有解。
    2.若knap(weight-s[n-1],n-1)即考虑第n件物品有解，那么knap(weight,n)就有解。
"""
from typing import List


def knapsack(weight: int, s: List[int], n: int):
    if weight == 0:
        return True
    if weight < 0 or (weight > 0 and n < 1):
        return False
    if knapsack(weight, s, n - 1):
        return True
    if knapsack(weight - s[n - 1], s, n - 1):
        print(f"Item:{n}", end="  ")
        return True
    else:
        return False


if __name__ == '__main__':
    if_can = knapsack(10, [5, 6, 2, 6, 2, 3, 1, 7, 2], 9)  # Item: 2  Item: 3  Item: 5
    print(f"\n{if_can}")  # True
