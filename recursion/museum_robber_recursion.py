#!/user/bin/python
# -*-coding:UTF-8-*-


"""博物馆大盗问题（递归解法）
问题描述：大盗嵌入博物馆，面前有五件宝物，分别有重量和价值，大盗的背包仅能负重20公斤，
请问如何选择宝物，总价值最高？
"""
from typing import Tuple, Dict


def museum_robber_recursion(max_weight_: int, items_: Tuple[Tuple[int, int]], item_used_: Dict[Tuple, int]):
    if items_ == set() or max_weight_ == 0:
        item_used_[(tuple(items_), max_weight_)] = 0
        return 0

    if (tuple(items_), max_weight_) in item_used_:
        return item_used_[(tuple(items_), max_weight_)]

    max_value = 0
    for item in items_:
        if item[0] <= max_weight_:
            v = museum_robber_recursion(max_weight_ - item[0], items_ - {item}, item_used_) + item[1]
            max_value = max(v, max_value)

    return max_value


if __name__ == '__main__':
    # 背包的能装的最大重量
    max_weight = 20

    # 宝物集合
    items = {
        (2, 3),
        (3, 4),
        (4, 8),
        (5, 8),
        (9, 10),
    }

    print(museum_robber_recursion(max_weight, items, {}))  # 29
