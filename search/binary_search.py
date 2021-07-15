#!/user/bin/python
# -*-coding:UTF-8-*-


"""二分搜索"""
from typing import List


def binary_search_recursion(alst: List, target):
    """二分查找的递归实现"""
    if not alst:
        return False

    middle = len(alst) // 2
    if alst[middle] == target:
        return True
    elif alst[middle] < target:
        return binary_search(alst[middle + 1:len(alst)], target)
    elif alst[middle] > target:
        return binary_search(alst[0:middle], target)


def binary_search(alst: List, target):
    """二分查找"""
    first = 0
    last = len(alst) - 1

    while first <= last:
        midpoint = (first + last) // 2
        if alst[midpoint] == target:
            return True
        elif target > alst[midpoint]:
            first = midpoint + 1
        elif target < alst[midpoint]:
            last = midpoint - 1

    return False


if __name__ == '__main__':
    print(binary_search_recursion([1, 3, 5, 7, 9, 15], 5))  # True
    print(binary_search_recursion([1, 3, 5, 7, 9, 15], 6))  # False

    print(binary_search([1, 3, 5, 7, 9, 15], 5))  # True
    print(binary_search([1, 3, 5, 7, 9, 15], 6))  # False
