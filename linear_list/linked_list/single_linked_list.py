#!/user/bin/python
# -*-coding:UTF-8-*-


"""单链表"""
import random


class LinkedListUnderflow(ValueError):
    pass


class LinkedListOverflow(ValueError):
    pass


class LNode(object):
    """单链表节点"""

    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next_: LNode = next_


class LList(object):
    def __init__(self):
        self._head: LNode = None
        self._num = 0

    def is_empty(self) -> bool:
        """判断链表是否为空"""
        return self._head is None

    def length(self) -> int:
        """返回链表的长度"""
        return self._num

    def append(self, elem):
        """向链表尾部插入元素"""
        if self._head is None:
            self._head = LNode(elem)
        else:
            p = self._head
            while p.next_ is not None:
                p = p.next_

            p.next_ = LNode(elem)
        self._num += 1

    def insert(self, elem, i_: int):
        """向链表指定位置插入元素"""
        if not isinstance(i_, int):
            raise TypeError("i must be int")
        if i_ < 0:
            raise LinkedListUnderflow("i must greater than or equal to 0")
        if i_ > self._num:
            raise LinkedListOverflow("i must less than or equal to list's length")

        if i_ == 0:
            self._head = LNode(elem, next_=self._head)
        else:
            p = self._head
            while i_ - 1 > 0:
                p = p.next_
                i_ = i_ - 1
            p.next_ = LNode(elem, p.next_)

        self._num += 1

    def del_first(self):
        """删除表中的第一个元素"""
        if self._head is None:
            raise LinkedListUnderflow("list is null")

        del_item = self._head.elem
        self._head = self._head.next_
        self._num -= 1

        return del_item

    def del_last(self):
        """删除表中最后一个元素"""
        if self._head is None:
            raise LinkedListUnderflow("list is null.")

        if self._head.next_ is None:
            del_item = self._head.elem
            self._head.next_ = None
        else:
            p = self._head
            while p.next_.next_ is not None:
                p = p.next_
            del_item = p.next_.elem
            p.next_ = None

        self._num -= 1
        return del_item

    def pop(self, i_: int):
        """删除指定位置的元素"""
        if i_ < 0:
            raise LinkedListUnderflow("i must greater than or equal to 0")
        if i_ >= self._num:
            raise LinkedListOverflow("i must be less than list's length")

        if i_ == 0:
            del_item = self._head.elem
            self._head = self._head.next_
        else:
            p = self._head
            while i_ - 1 > 0:
                p = p.next_
                i_ = i_ - 1
            del_item = p.next_.elem
            p.next_ = p.next_.next_

        self._num -= 1
        return del_item

    def clear(self):
        """清空链表"""
        self._head = None

    def elements(self):
        """迭代器"""
        p = self._head
        while p is not None:
            yield p.elem
            p = p.next_

    def search(self, elem):
        """搜索元素elem的位置"""
        p = self._head
        i_ = 0
        while p is not None:
            if p.elem == elem:
                return i_
            p = p.next_
            i_ += 1
        return -1

    def reverse(self):
        """反转链表"""
        if self._head is None or self._head.next_ is None:
            return
        q = None
        while self._head is not None:
            p = self._head
            self._head = self._head.next_
            p.next_ = q
            q = p

        self._head = q

    def del_minimal(self):
        """删除链表中的最小元素"""
        if self._head is None:
            raise LinkedListUnderflow("i must greater than or equal to 0")
        if self._head.next_ is None:
            del_item = self._head.elem
            self._head = None
        else:
            q = None
            del_item = self._head.elem
            p = self._head
            while p.next_ is not None:
                if p.next_.elem < del_item:
                    del_item = p.next_.elem
                    q = p
                p = p.next_

            if q is not None:
                q.next_ = q.next_.next_
            else:
                self._head = self._head.next_

        self._num -= 1
        return del_item

    def del_duplicate(self):
        """删除表中重复元素"""
        q = None
        p = self._head
        exit_items = set()
        while p is not None:
            if p.elem in exit_items:
                q.next_ = p.next_
                self._num -= 1
            else:
                q = p
                exit_items.add(p.elem)
            p = p.next_

    def sort(self):
        """通过搬移数据的方式插入排序"""
        if self._head is None or self._head.next_ is None:
            return

        crt = self._head.next_
        while crt is not None:
            x = crt.elem
            p = self._head
            while p is not crt and x >= p.elem:
                p = p.next_
            while p is not crt:
                y = p.elem
                p.elem = x
                x = y  # 倒换大元素
                p = p.next_
            crt.elem = x
            crt = crt.next_

    def sort2(self):
        """通过搬移节点的方式进行插入排序"""
        if self._head is None or self._head.next_ is None:
            return
        p = self._head
        while p is not None and p.next_ is not None:
            k = None
            q = self._head
            while q is not p.next_ and p.next_.elem >= q.elem:
                k = q
                q = q.next_

            if q is not p.next_:
                node, p.next_ = p.next_, p.next_.next_
                if k is None:
                    node.next_, self._head = q, node
                else:
                    k.next_, node.next_ = node, q
            else:
                p = p.next_

    def __len__(self):
        return self.length()

    def __getitem__(self, item):
        if item < 0:
            raise LinkedListUnderflow("i must greater than or equal to 0")
        if item >= self._num:
            raise LinkedListOverflow("i must be less than list's length")

        p = self._head
        while item > 0:
            p = p.next_
            item -= 1

        return p.elem

    def __setitem__(self, key, value):
        if key < 0:
            raise LinkedListUnderflow("i must greater than or equal to 0")
        if key >= self._num:
            raise LinkedListOverflow("i must be less than list's length")

        p = self._head
        while key - 1 > 0:
            p = p.next_
            key -= 1

        p.next_.elem = value

    def __getattr__(self, item):
        if item < 0:
            raise LinkedListUnderflow("i must greater than or equal to 0")
        if item >= self._num:
            raise LinkedListOverflow("i must be less than list's length")

        p = self._head
        while item > 0:
            p = p.next_
            item -= 1

        return p.elem

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


llist = LList()
for i in range(1, 10):
    llist.append(i)
print(llist.length())  # 9
print(llist)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range(1, 10):
    llist.append(random.randint(0, i))
print(llist.length())  # 18
print(llist)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 2, 2, 0, 3, 5, 5, 3, 6]
llist.del_duplicate()
print(llist.length())  # 10
print(llist)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

print(llist.del_first())  # 1
print(llist.length())  # 9
print(llist)  # [2, 3, 4, 5, 6, 7, 8, 9, 0]

print(llist.del_last())  # 0
print(llist.length())  # 8
print(llist)  # [2, 3, 4, 5, 6, 7, 8, 9]

print(llist.del_minimal())  # 2
print(llist.length())  # 7
print(llist)  # [3, 4, 5, 6, 7, 8, 9]

llist.insert(1, 0)
llist.insert(2, 1)
llist.insert(10, llist.length())
print(llist.length())  # 10
print(llist)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(llist.pop(2))  # 3
print(llist.length())  # 9
print(llist)  # [1, 2, 4, 5, 6, 7, 8, 9, 10]

llist.reverse()
print(llist)  # [10, 9, 8, 7, 6, 5, 4, 2, 1]

print(llist.search(9))  # 1

llist.sort2()
print(llist)  # [1, 2, 4, 5, 6, 7, 8, 9, 10
