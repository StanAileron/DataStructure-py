#!/user/bin/python
# -*-coding:UTF-8-*-


"""冒泡排序"""
from typing import List


def bubble_sort(alst: List):
    for i in range(len(alst) - 1):  # 当只有一个元素时不需要比较，因此只需要遍历n-1次。
        exchange = False
        for j in range(1, len(alst) - i):
            if alst[j - 1] > alst[j]:
                alst[j - 1], alst[j] = alst[j], alst[j - 1]
                exchange = True

        if not exchange:  # 在这次遍历中没有发生元素交换，说明已经排序好了
            break


if __name__ == '__main__':
    test_lst = [1, 3, 6, 2, 6, 7, 3, 7, 9, 0, 1, 3, 5, 7, 3, 4]
    bubble_sort(test_lst)
    print(test_lst)
    # [0, 1, 1, 2, 3, 3, 3, 3, 4, 5, 6, 6, 7, 7, 7, 9]
