#!/user/bin/python
# -*-coding:UTF-8-*-


"""实现快速排序(为基准值寻找正确位置过程的示意图参加（注意，要从左右同时向中间逼近）)
一. 为基准值为找正确的位置（所有小于等于基准值的元素放在基准值的左边，所有大于基准值的元素放在基准值的右边）：
    1. 将列表的第一个元素定义为基准值，设置left和right分别表示剩余元素的开头和结尾。
    2.  （1）比较left和基准值的大小，若基准值>=left，则left右移一位；否则，left止步。
        （2）然后比较right和基准值的大小，若基准值<=right，则right左移以为；否则，right止步，并且交换left元素和right元素的值。
        （3）判断left元素和right元素的下标的大小，
                若left<=right，则重复步骤2；
                若left>right，则交换right和基准值，并且设置基准值的元素下标为right的下标。以基准值为分割点划分列表，并且递归地调用左列表和右列表。

"""
from typing import List


def partition(alst: List, start: int, end: int) -> int:
    pivotvalue = alst[start]
    leftmark = start + 1
    rightmark = end

    done = False
    while not done:
        # 不能同时设置：alst[leftmark] < pivotvalue 和 alst[rightmark] > pivotvalue, 
        # 否则会一直交换leftmart和rightmart处的值，陷入死循环。
        # 因此，必须至少设置alst[leftmark] <= pivotvalue或者alst[rightmark] >= pivotvalue。
        while leftmark <= rightmark and alst[leftmark] <= pivotvalue:
            leftmark += 1

        while leftmark <= rightmark and alst[rightmark] > pivotvalue:
            rightmark -= 1

        # 这里一定是进行小于等于判断，否则有可能alst[rightmark]值大于als[start]值，造成基准值放置失败。
        if leftmark <= rightmark:
            alst[leftmark], alst[rightmark] = alst[rightmark], alst[leftmark]
        else:
            done = True

    alst[start], alst[rightmark] = alst[rightmark], alst[start]
    return rightmark


def quick_sort_helper(alst: List, start: int, end: int):
    if start < end:
        splitpoint = partition(alst, start, end)

        quick_sort_helper(alst, start, splitpoint - 1)
        quick_sort_helper(alst, splitpoint + 1, end)


def quick_sort(alst: List):
    quick_sort_helper(alst, 0, len(alst) - 1)


if __name__ == '__main__':
    test_lst = [1, 5, 6, 3, 54, 7, 3, 2, 5, 21, 67, 9, 2, 6, 2]
    quick_sort(test_lst)
    print(test_lst)  # [1, 2, 2, 2, 3, 3, 5, 5, 6, 6, 7, 9, 21, 54, 67]
