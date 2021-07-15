#!/user/bin/python
# -*-coding:UTF-8-*-


"""实现选择排序"""
from typing import List


def select_sort(alst: List):
    for i in range(len(alst) - 1):
        max_idx = 0  # 最大元素的下标
        for j in range(1, len(alst) - i):
            if alst[j] > alst[max_idx]:
                max_idx = j

        # 将最大的元素交换到末尾
        alst[max_idx], alst[len(alst) - i - 1] = alst[len(alst) - i - 1], alst[max_idx]


if __name__ == '__main__':
    test_lst = [1, 3, 6, 2, 6, 7, 3, 7, 9, 0, 1, 3, 5, 7, 3, 4]
    select_sort(test_lst)
    print(test_lst)
    # [0, 1, 1, 2, 3, 3, 3, 3, 4, 5, 6, 6, 7, 7, 7, 9]
