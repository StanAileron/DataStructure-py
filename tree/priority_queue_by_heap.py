#!/user/bin/python
# -*-coding:UTF-8-*-


"""使用二叉堆实现优先队列
1. 二叉堆的定义：是节点中存储数据的完全二叉树，并且满足一种特殊的堆序：任一节点中存储的数据先于或等于其子节点中的数据。
    如果要求的序是小元素优先，则称其为小顶堆；如果要求的序是大元素优先，则称其为大顶堆。
2. 完全二叉树可以自然地映射为一个数组/列表。
"""
import random


class PriorityQueueError(ValueError):
    pass


class PriorityQueue:
    def __init__(self, elist=[]):
        self._elems = list(elist)
        self._build_heap()

    def _build_heap(self):
        start_sift = len(self._elems) // 2
        for i_ in range(start_sift, -1, -1):
            self._sift_down(self._elems[i_], i_, len(self._elems))

    def is_empty(self):
        return self._elems == []

    def peek(self):
        if self.is_empty():
            raise PriorityQueueError("the queue is null")
        return self._elems[0]

    def enqueue(self, elem):
        self._elems.append(None)
        self._sift_up(elem)

    def _sift_up(self, elem):
        """执行向上筛选，让完全二叉树保持堆序"""
        i_ = len(self._elems) - 1
        j = (i_ - 1) // 2

        while i_ > 0 and self._elems[j] > elem:
            self._elems[i_] = self._elems[j]
            i_, j = j, (j - 1) // 2

        self._elems[i_] = elem

    def dequeue(self):
        if self.is_empty():
            raise PriorityQueueError("the queue is error")

        dequeue_elem = self._elems[0]
        sift_elem = self._elems.pop()
        if not self.is_empty():
            self._sift_down(sift_elem, 0, len(self._elems))

        return dequeue_elem

    def _sift_down(self, elem, start, end):
        """执行向下筛选，让完全二叉树保持堆序"""
        i_ = start
        j = 2 * i_ + 1

        while j < end:
            if j + 1 < end and self._elems[j + 1] < self._elems[j]:
                j = j + 1
            if elem <= self._elems[j]:
                break
            self._elems[i_] = self._elems[j]
            i_, j = j, 2 * j + 1

        self._elems[i_] = elem


if __name__ == '__main__':
    pq = PriorityQueue([1, 10, 2, 5, 4, 2, 6, 6, 9, 3])

    while not pq.is_empty():
        print(pq.dequeue(), end=' ')
    print()
    # 1 2 2 3 4 5 6 6 9 10

    for i in range(10):
        pq.enqueue(random.randint(-1, i))

    while not pq.is_empty():
        print(pq.dequeue(), end=' ')
    print()
    # -1 -1 -1 0 2 2 3 3 5 9
