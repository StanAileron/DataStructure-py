#!/user/bin/python
# -*-coding:UTF-8-*-


"""希尔排序"""
from typing import List


def shell_sort(alst: List):
    sublist_count = len(alst) // 2

    while sublist_count > 0:
        # 对划分的每个子列表进行插入排序
        for start_positon in range(sublist_count):
            gap_insert_sort(alst, start_positon, sublist_count)

        print("After increments of size", sublist_count, "The list is", alst)

        sublist_count = sublist_count // 2


def gap_insert_sort(alst: List, start: int, gap: int):
    for i in range(start + gap, len(alst), gap):
        j = i - gap

        elem = alst[i]
        while j >= 0:
            if alst[j] > elem:
                alst[i] = alst[j]
                i, j = i - gap, j - gap
            else:
                alst[i] = elem
                break


if __name__ == '__main__':
    test_lst = [1, 5, 6, 3, 54, 7, 3, 2, 5, 21, 67, 9, 2, 6, 2]
    shell_sort(test_lst)

# After increments of size 7 The list is [1, 5, 6, 3, 54, 7, 3, 2, 5, 21, 67, 54, 7, 6, 2]
# After increments of size 3 The list is [1, 5, 6, 3, 5, 6, 3, 6, 6, 7, 54, 7, 21, 67, 54]
# After increments of size 1 The list is [1, 3, 3, 5, 5, 6, 6, 6, 6, 7, 7, 21, 54, 54, 67]
