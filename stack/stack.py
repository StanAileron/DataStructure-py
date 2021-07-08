#!/user/bin/python
# -*-coding:UTF-8-*-


"""实现stack"""
from linear_list.linked_list.single_linked_list import LList


class StackUnderFlow(ValueError):
    pass


# 使用顺序表实现栈
class Stack:
    def __init__(self):
        self._items = []

    def is_empty(self):
        return self._items == []

    def push(self, elem):
        self._items.append(elem)

    def pop(self):
        if self.is_empty():
            raise StackUnderFlow("in stack.pop()")
        return self._items.pop()

    def top(self):
        if self.is_empty():
            raise StackUnderFlow("in stack.pop()")
        return self._items[-1]

    def length(self):
        return len(self._items)


# 使用链表实现栈
class StackByLink:
    def __init__(self):
        self._items = LList()

    def is_empty(self):
        return self._items.is_empty()

    def push(self, elem):
        self._items.prepend(elem)

    def pop(self):
        return self._items.del_first()

    def top(self):
        return self._items[0]

    def length(self):
        return self._items.length()


if __name__ == '__main__':
    s1 = Stack()
    for i in range(5):
        s1.push(i)
    print(s1.length())  # 5

    for i in range(5):
        if not s1.is_empty():
            if s1.length() == 1:
                print(s1.pop())
            else:
                print(s1.pop(), end=" ")
            # 4 3 2 1 0
    print(s1.length())  # 0

    s2 = StackByLink()
    for i in range(5):
        s2.push(i)
    print(s2.length())  # 5

    for i in range(5):
        if not s2.is_empty():
            if s2.length() == 1:
                print(s2.pop())
            else:
                print(s2.pop(), end=" ")
            # 4 3 2 1 0
    print(s2.length())  # 0
