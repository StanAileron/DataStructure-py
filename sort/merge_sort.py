#!/user/bin/python
# -*-coding:UTF-8-*-


"""归并牌序（拆分列表、合并列表的示意图参见：merge_sort.png）
时间复杂度为O(nlog n)
"""
from typing import List


def merge_sort(alst: List):
    print("Splitting ", alst)
    if len(alst) > 1:
        mid = len(alst) // 2
        left_lst = alst[:mid]
        right_lst = alst[mid:]

        merge_sort(left_lst)
        merge_sort(right_lst)

        i = 0
        j = 0
        k = 0
        while i < len(left_lst) and j < len(right_lst):
            if left_lst[i] < right_lst[j]:
                alst[k] = left_lst[i]
                i = i + 1
            else:
                alst[k] = left_lst[j]
                j = j + 1
            k = k + 1

        # 要么left_lst有剩余元素，要么right_lst有剩余元素，剩余的元素一定大于alst[k-1]
        while i < len(left_lst):
            alst[k] = left_lst[i]
            i = i + 1
            k = k + 1

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
# Splitting  [5, 6]
# Splitting  [5]
# Splitting  [6]
# Merging  [5, 6]
# Merging  [1, 5, 6]
# Splitting  [3, 54, 7, 3]
# Splitting  [3, 54]
# Splitting  [3]
# Splitting  [54]
# Merging  [3, 54]
# Splitting  [7, 3]
# Splitting  [7]
# Splitting  [3]
# Merging  [7, 7]
# Merging  [3, 3, 54, 54]
# Merging  [1, 1, 5, 5, 6, 54, 54]
# Splitting  [2, 5, 21, 67, 9, 2, 6, 2]
# Splitting  [2, 5, 21, 67]
# Splitting  [2, 5]
# Splitting  [2]
# Splitting  [5]
# Merging  [2, 5]
# Splitting  [21, 67]
# Splitting  [21]
# Splitting  [67]
# Merging  [21, 67]
# Merging  [2, 5, 21, 67]
# Splitting  [9, 2, 6, 2]
# Splitting  [9, 2]
# Splitting  [9]
# Splitting  [2]
# Merging  [9, 9]
# Splitting  [6, 2]
# Splitting  [6]
# Splitting  [2]
# Merging  [6, 6]
# Merging  [9, 9, 9, 9]
# Merging  [2, 5, 2, 5, 21, 67, 21, 67]
# Merging  [1, 1, 1, 1, 5, 5, 5, 5, 6, 6, 54, 54, 67, 21, 67]
