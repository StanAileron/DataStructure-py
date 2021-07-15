#!/user/bin/python
# -*-coding:UTF-8-*-


"""顺序搜索"""
from typing import List


def sequential_search(alst: List, item):
    for i in range(len(alst)):
        if alst[i] == item:
            return True

    return False


def ordered_sequantial_search(alst: List, item):
    for i in range(len(alst)):
        if alst[i] == item:
            return True
        elif alst[i] > item:
            return False
        else:
            pass
    return False


if __name__ == '__main__':
    print(sequential_search([1, 2, 3, 4, 5], 3))  # True
    print(sequential_search([1, 2, 3, 4, 5], 10))  # False

    print(ordered_sequantial_search([1, 3, 5, 7, 10], 5))  # True
    print(ordered_sequantial_search([1, 3, 5, 7, 10], 4))  # False
