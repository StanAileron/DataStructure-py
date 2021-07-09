#!/user/bin/python
# -*-coding:UTF-8-*-


"""实现队列"""
from linear_list.linked_list.single_linked_list import LList


class QueueUnderFlow(ValueError):
    pass


# 使用顺序表实现循环队列
class SQueue:
    def __init__(self, init_lens=8):
        self._len = init_lens  # 队列最大长度
        self._elems = [None] * self._len
        self._num = 0  # 当前队列长度
        self._head = 0  # 队列头部下标

    def is_empty(self):
        return self._num == 0

    def size(self):
        return self._num

    def enqueue(self, elem):
        if self._num == self._len:
            self._extend()
        self._elems[(self._head + self._num) % self._len] = elem
        self._num += 1

    def dequeue(self):
        if self.is_empty():
            raise QueueUnderFlow("in SQueue.dequeue()")
        elem = self._elems[self._head]
        self._head = (self._head + 1) % self._len
        self._num -= 1
        return elem

    def peek(self):
        if self.is_empty():
            raise QueueUnderFlow("in SQueue.dequeue()")
        return self._elems[self._head]

    def _extend(self):
        new_len = self._len * 2
        new_elems = [None] * new_len
        for i in range(self._num):
            new_elems[i] = self._elems[(i + self._head) % self._len]
        self._elems = new_elems
        self._len = new_len
        self._head = 0

    def __str__(self):
        lst = ["["]
        rear = self._head + self._num
        for i_ in range(self._head, rear):
            if i_ == rear - 1:
                lst.append(f"{self._elems[i_ % self._len]}]")
            else:
                lst.append(f"{self._elems[i_ % self._len]}, ")
        return "".join(lst)


# 使用单链表实现队列
class SQueueByLink:
    def __init__(self):
        self._elems = LList()

    def is_empty(self):
        return self._elems.is_empty()

    def size(self):
        return self._elems.length()

    def enqueue(self, elem):
        self._elems.append(elem)

    def dequeue(self):
        return self._elems.del_first()

    def peek(self):
        return self._elems[0]

    def __str__(self):
        return str(self._elems)


if __name__ == '__main__':
    s1 = SQueue()
    for i in range(5):
        s1.enqueue(i)
    print(s1.size())  # 5
    print(s1)  # [0, 1, 2, 3, 4]
    for i in range(5):
        print(s1.dequeue(), end=" ")  # 0 1 2 3 4

    print()

    s2 = SQueueByLink()
    for i in range(5):
        s2.enqueue(i)
    print(s2.size())  # 5
    print(s2)  # [0, 1, 2, 3, 4]
    for i in range(5):
        print(s2.dequeue(), end=" ")  # 0 1 2 3 4
