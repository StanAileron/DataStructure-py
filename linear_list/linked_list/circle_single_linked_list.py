#!/user/bin/python
# -*-coding:UTF-8-*-


"""循环单链表"""


class LNode:
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next_ = next_


class LCList:
    def __init__(self):
        self._rear = None   # 尾节点

    def is_empty(self):
        return self._rear is None

    def length(self):
        if self._rear is None:
            return 0
        num = 1
        p = self._rear.next_
        while p is not self._rear:
            p = p.next_
            num += 1

        return num

    def prepend(self, elem):
        """向表首添加元素"""
        p = LNode(elem)
        if self._rear is None:
            p.next_ = p
            self._rear = p
        else:
            p.next_ = self._rear.next_
            self._rear.next_ = p

    def append(self, elem):
        """向表尾添加元素"""
        p = LNode(elem)
        if self._rear is None:
            p.next_ = p
        else:
            p.next_ = self._rear.next_
            self._rear.next_ = p

        self._rear = p

    def del_first(self):
        """删除表首元素"""
        if self._rear is None:
            raise ValueError("list is null")

        del_item = self._rear.next_.elem
        if self._rear.next_ is self._rear:
            self._rear = None
        else:
            self._rear.next_ = self._rear.next_.next_
        return del_item

    def del_last(self):
        """删除表尾元素"""
        if self._rear is None:
            raise ValueError("list is null")

        del_item = self._rear.elem
        p = self._rear.next_
        if p is self._rear:
            self._rear = None
        else:
            while p.next_ is not self._rear:
                p = p.next_
            p.next_ = self._rear.next_
            self._rear = p
        return del_item

    def pop(self, idx):
        """删除指定位置的元素"""
        if idx < 0:
            raise IndexError("idx must greater than or equal to 0")
        if idx >= self.length():
            raise IndexError("idx must less than list's length")

        if idx == 0:
            p = self._rear.next_
            del_item = p.elem
            if p is self._rear:
                self._rear = None
            else:
                self._rear.next_ = p.next_
        else:
            p = self._rear.next_
            while idx - 1 > 0:
                p = p.next_
                idx -= 1

            del_item = p.next_.elem
            if p.next_ is self._rear:
                p.next_ = self._rear.next_
                self._rear = p
            else:
                p.next_ = p.next_.next_

        return del_item

    def __len__(self):
        return self.length()

    def __str__(self):
        print_list = ["["]
        p = self._rear.next_
        while p is not self._rear:
            if p.next_ is self._rear:
                print_list.append(f"{p.elem}, {self._rear.elem}]")
            else:
                print_list.append(f"{p.elem}, ")
            p = p.next_

        return "".join(print_list)


lst = LCList()
for i in range(5, -1, -1):
    lst.prepend(i)
print(len(lst)) # 6
print(lst)  # [0, 1, 2, 3, 4, 5]

for i in range(6, 10):
    lst.append(i)
print(len(lst)) # 10
print(lst)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(lst.del_first())  # 0
print(len(lst)) # 9
print(lst)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(lst.del_last())   # 8
print(len(lst)) # 9
print(lst)  # [1, 2, 3, 4, 5, 6, 7, 8]

print(lst.pop(2))   # 3
print(len(lst)) # 7
print(lst)  # [1, 2, 4, 5, 6, 7, 8]