#!/user/bin/python
# -*-coding:UTF-8-*-


"""归并牌序（拆分列表、合并列表的示意图参见：merge_sort.png）
时间复杂度为O(nlog n)
"""
from typing import List


def merge_sort(alst: List):
    print("Splitting ", alst)
    if len(alst) > 1:  # 基本结束条件
        mid = len(alst) // 2
        left_lst = alst[:mid]
        right_lst = alst[mid:]

        merge_sort(left_lst)
        merge_sort(right_lst)

        i = j = k = 0
        # 拉链式交错把左半部分从小到大归并到结果列表中
        while i < len(left_lst) and j < len(right_lst):
            if left_lst[i] < right_lst[j]:
                alst[k] = left_lst[i]
                i = i + 1
            else:
                alst[k] = right_lst[j]
                j = j + 1
            k = k + 1

        # 归并左半部剩余项
        while i < len(left_lst):
            alst[k] = left_lst[i]
            i = i + 1
            k = k + 1

        # 归并右半部剩余项
        while j < len(right_lst):
            alst[k] = right_lst[j]
            j = j + 1
            k = k + 1

    print("Merging ", alst)


if __name__ == '__main__':
    test_lst = [1, 5, 6, 3, 54, 7, 3, 2, 5, 21, 67, 9, 2, 6, 2]
    merge_sort(test_lst)

# Splitting  [1, 5, 6, 3, 54, 7, 3, 2, 5, 21, 67, 9, 2, 6, 2]
# Splitting  [1, 5, 6, 3, 54, 7, 3]
# Splitting  [1, 5, 6]
# Splitting  [1]
# Merging  [1]
# Splitting  [5, 6]
# Splitting  [5]
# Merging  [5]
# Splitting  [6]
# Merging  [6]
# Merging  [5, 6]
# Merging  [1, 5, 6]
# Splitting  [3, 54, 7, 3]
# Splitting  [3, 54]
# Splitting  [3]
# Merging  [3]
# Splitting  [54]
# Merging  [54]
# Merging  [3, 54]
# Splitting  [7, 3]
# Splitting  [7]
# Merging  [7]
# Splitting  [3]
# Merging  [3]
# Merging  [3, 7]
# Merging  [3, 3, 7, 54]
# Merging  [1, 3, 3, 5, 6, 7, 54]
# Splitting  [2, 5, 21, 67, 9, 2, 6, 2]
# Splitting  [2, 5, 21, 67]
# Splitting  [2, 5]
# Splitting  [2]
# Merging  [2]
# Splitting  [5]
# Merging  [5]
# Merging  [2, 5]
# Splitting  [21, 67]
# Splitting  [21]
# Merging  [21]
# Splitting  [67]
# Merging  [67]
# Merging  [21, 67]
# Merging  [2, 5, 21, 67]
# Splitting  [9, 2, 6, 2]
# Splitting  [9, 2]
# Splitting  [9]
# Merging  [9]
# Splitting  [2]
# Merging  [2]
# Merging  [2, 9]
# Splitting  [6, 2]
# Splitting  [6]
# Merging  [6]
# Splitting  [2]
# Merging  [2]
# Merging  [2, 6]
# Merging  [2, 2, 6, 9]
# Merging  [2, 2, 2, 5, 6, 9, 21, 67]
# Merging  [1, 2, 2, 2, 3, 3, 5, 5, 6, 6, 7, 9, 21, 54, 67]
