#!/user/bin/python
# -*-coding:UTF-8-*-


"""循环双链表"""


class Node:
    def __init__(self, elem, prev: "Node" = None, next_: "Node" = None):
        self.elem = elem
        self.prev = prev
        self.next_ = next_


class CyDoubleLinkList:
    def __init__(self):
        self._head: Node = None
        self._rear: Node = None

    def prepend(self, elem):
        """向表首插入元素"""
        p = Node(elem, prev=self._rear, next_=self._head)
        if self._head is None:
            p.next_, p.prev = p, p
            self._rear = p
        else:
            self._rear.next_ = p
            self._head.prev = p
        self._head = p

    def append(self, elem):
        """向表尾插入元素"""
        p = Node(elem, prev=self._rear, next_=self._head)
        if self._head is None:
            p.next_, p.prev = p, p
        else:
            self._rear.next_ = p
            self._head.prev = p
        self._rear = p

    def insert(self, elem, idx: int):
        if not isinstance(idx, int):
            raise TypeError("idx must be integer")
        if idx < 0 or idx > self.length():
            raise IndexError("idx must greater >= 0 and <= list's length")

        if idx == 0:
            self.prepend(elem)
        elif idx == self.length():
            self.append(elem)
        else:
            new_node = Node(elem)
            p = self._head
            while idx > 0:
                p = p.next_
                idx -= 1
            q = p.prev
            q.next_, new_node.prev = new_node, q
            new_node.next_, p.prev = p, new_node

    def del_first(self):
        if self._head is None:
            raise ValueError("list is null")

        del_elem = self._head.elem
        if self._head is self._rear:
            self._head: Node = None
            self._rear: Node = None
        else:
            p = self._head.next_
            p.prev, self._rear.next_, self._head = self._rear, p, p

        return del_elem

    def del_last(self):
        if self._head is None:
            raise ValueError("list is null")

        del_elem = self._rear.elem
        if self._head is self._rear:
            self._head: Node = None
            self._rear: Node = None
        else:
            p = self._rear.prev
            p.next_, self._head.prev, self._rear = self._head, p, p

        return del_elem

    def pop(self, idx):
        if not isinstance(idx, int):
            raise TypeError("idx must be integer")
        if idx < 0 or idx >= self.length():
            raise IndexError("idx must greater >= 0 and < list's length")

        if idx == 0:
            return self.del_first()
        elif idx == self.length() - 1:
            return self.del_last()
        else:
            p = self._head
            while idx > 0:
                p = p.next_
                idx -= 1
            p.prev.next_, p.next_.prev = p.next_, p.prev
            return p.elem

    def length(self):
        p = self._head
        if p is None:
            return 0
        _sum = 1
        while p is not self._rear:
            _sum += 1
            p = p.next_
        return _sum

    def is_empty(self):
        return self._head is None

    def __str__(self):
        print_list = ["["]
        p = self._head
        while p is not self._rear:
            if p.next_ is self._rear:
                print_list.append(f"{p.elem}, {self._rear.elem}]")
            else:
                print_list.append(f"{p.elem}, ")
            p = p.next_

        return "".join(print_list)


lst = CyDoubleLinkList()

for i in range(5, -1, -1):
    lst.prepend(i)
print(lst.length())  # 6
print(lst)  # [0, 1, 2, 3, 4, 5]

for i in range(6, 10):
    lst.append(i)
print(lst.length())  # 10
print(lst)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

lst.insert(2.5, 3)
print(lst.length())  # 11
print(lst)  # [0, 1, 2, 2.5, 3, 4, 5, 6, 7, 8, 9]

print(lst.del_first())  # 0
print(lst.length())  # 10
print(lst)  # [1, 2, 2.5, 3, 4, 5, 6, 7, 8, 9]

print(lst.del_last())  # 9
print(lst.length())  # 9
print(lst)  # [1, 2, 2.5, 3, 4, 5, 6, 7, 8]

print(lst.pop(2))  # 2.5
print(lst.length())  # 8
print(lst)  # [1, 2, 3, 4, 5, 6, 7, 8]
