#!/user/bin/python
# -*-coding:UTF-8-*-


"""博物馆大盗问题（动态规划解法）
问题描述：大盗嵌入博物馆，面前有五件宝物，分别有重量和价值，大盗的背包仅能负重20公斤，
请问如何选择宝物，总价值最高？
"""
from typing import Tuple, Dict


def musuem_robber(items_: Tuple[Dict[int, int]], max_weight_: int, max_values_: Dict[Tuple[int, int], int]):
    for i in range(len(items_)):
        for weight in range(max_weight_ + 1):
            if i == 0 or weight == 0:
                max_values_[(i, weight)] = 0
            elif items_[i]["w"] > weight:
                max_values_[(i, weight)] = max_values_[(i - 1, weight)]
            else:
                max_values_[(i, weight)] = max(
                    max_values_[(i - 1, weight)],
                    max_values_[(i - 1, weight - items_[i]["w"])] + items_[i]["v"]
                )


if __name__ == '__main__':
    # 背包的能装的最大重量
    max_weight = 20

    # 宝物集合
    items = (
        {"w": 0, "v": 0},
        {"w": 2, "v": 3},
        {"w": 3, "v": 4},
        {"w": 4, "v": 8},
        {"w": 5, "v": 8},
        {"w": 9, "v": 10},
    )

    # 初始二维表格(每个背包重量和宝物组合对应的最大价值)
    max_values = {(i, j): 0 for i in range(len(items)) for j in range(max_weight + 1)}

    musuem_robber(items, max_weight, max_values)

    print(max_values[(5, 20)])  # 29
