#!/user/bin/python
# -*-coding:UTF-8-*-


"""双链表"""
import random


class Node(object):
    def __init__(self, elem, prev=None, next_=None):
        self.elem = elem
        self.prev = prev
        self.next_ = next_


class DoubleLinkedList(object):
    def __init__(self):
        self._head = None
        self._rear = None

    def prepend(self, elem):
        """表首插入元素"""
        p = Node(elem, next_=self._head)
        if self._head is None:
            self._rear = p
        else:
            p.next_.prev = p
        self._head = p

    def append(self, elem):
        """表尾插入元素"""
        p = Node(elem)
        if self._head is None:
            self._head = p
        else:
            self._rear.next_ = p
            p.prev = self._rear
        self._rear = p

    def reverse1(self):
        """通过搬移数据的方式反转链表"""
        if self._head is None or self._head.next_ is None:
            return
        p = self._head
        q = self._rear
        while p != q and p.prev != q:
            p.elem, q.elem = q.elem, p.elem
            p, q = p.next_, q.prev

    def reverse2(self):
        """通过搬移节点的方式反转链表"""
        if self._head is None or self._head.next_ is None:
            return
        p = None
        while self._head is not None:
            q = self._head
            self._head = self._head.next_
            q.next_ = p
            if p is None:
                self._rear = q
            else:
                p.prev = q
            p = q
        self._head = p
        self._head.prev = None

    def sort(self):
        """通过搬移节点的方式插入排序"""
        if self._head is None or self._head.next_ is None:
            return

        crt = self._head.next_
        while crt is not None:
            p = self._head
            while p is not crt and p.elem <= crt.elem:
                p = p.next_

            q, crt = crt, crt.next_
            if p is not q:
                if q.next_ is None:
                    self._rear = q.prev
                    self._rear.next_ = None
                else:
                    q.next_.prev, q.prev.next_ = q.prev, q.next_

                q.prev, q.next_ = p.prev, p
                if q.prev is not None:
                    q.prev.next_ = q
                else:
                    self._head = q  # q.prev=None 说明q成为了新的q节点
                p.prev = q

    def __len__(self):
        p = self._head
        _sum = 0
        while p is not None:
            _sum += 1
            p = p.next_
        return _sum

    def __str__(self):
        print_list = ["["]
        p = self._head
        while p is not None:
            if p.next_ is None:
                print_list.append(f"{p.elem}]")
            else:
                print_list.append(f"{p.elem}, ")
            p = p.next_
        return "".join(print_list)


dl = DoubleLinkedList()

for i in range(5, -1, -1):
    dl.prepend(i)
print(len(dl))  # 6
print(dl)   # [0, 1, 2, 3, 4, 5]

for i in range(6, 10):
    dl.append(i)
print(len(dl))  # 10
print(dl)   # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

dl.reverse1()
print(dl)   # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

dl.reverse2()
print(dl)   # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

dl2 = DoubleLinkedList()
for i in range(10):
    dl2.append(random.randint(-1, i))
print(dl2)  # [0, 1, 1, 2, 1, 4, 5, 0, 0, 7]
dl2.sort()
print(dl2)  # [0, 0, 0, 1, 1, 1, 2, 4, 5, 7]
