#!/user/bin/python
# -*-coding:UTF-8-*-


"""插入排序"""
from typing import List


def insert_sort(alst: List):
    for i in range(1, len(alst)):
        j = i - 1
        elem = alst[i]
        while j >= 0:
            if alst[j] > elem:
                alst[i] = alst[j]
                j, i = j - 1, i - 1
            else:
                alst[i] = elem
                break


if __name__ == '__main__':
    test_lst = [1, 5, 6, 3, 54, 7, 3, 2, 5, 21, 67, 9, 2, 6, 2]
    insert_sort(test_lst)
    print(test_lst)  # [1, 2, 2, 2, 3, 3, 5, 5, 6, 6, 7, 9, 21, 54, 67]
