#!/user/bin/python
# -*-coding:UTF-8-*-


"""堆排序"""
from typing import List


def heap_sort(alst: List):
    def sift_down(elem, start, end):
        i_ = start
        j = 2 * start + 1

        while j < end:
            if j + 1 < end and alst[j + 1] < alst[j]:
                j = j + 1

            if elem < alst[j]:
                break
            alst[i_] = alst[j]
            i_, j = j, 2 * j + 1

        alst[i_] = elem

    sift_index = len(alst) // 2
    for i in range(sift_index, -1, -1):
        sift_down(alst[i], i, len(alst))

    for i in range(len(alst) - 1, 0, -1):
        sift_elem = alst[i]
        alst[i] = alst[0]
        sift_down(sift_elem, 0, i)


if __name__ == '__main__':
    test_lst = [1, 5, 6, 3, 54, 7, 3, 2, 5, 21, 67, 9, 2, 6, 2]
    heap_sort(test_lst)
    print(test_lst)  # [67, 54, 21, 9, 7, 6, 6, 5, 5, 3, 3, 2, 2, 2, 1]
