#!/user/bin/python
# -*-coding:UTF-8-*-

from typing import List, Any


# 使用嵌套列表表示二叉树
def binary_tree_by_list(r: Any):
    """创建树结构"""
    return [r, [], []]


def insert_left(root: List[List], new_val: Any):
    """插入左子树"""
    t = root.pop(1)
    if len(t) > 0:
        root.insert(1, [new_val, t, []])
    else:
        root.insert(1, [new_val, [], []])

    return root


def insert_right(root: List[List], new_val: Any):
    """插入右子树"""
    t = root.pop(2)
    if len(t) > 0:
        root.insert(2, [new_val, [], t])
    else:
        root.insert(2, [new_val, [], []])

    return root


def set_root_val(root: List[List], new_val: Any):
    root[0] = new_val


def get_root_val(root: List[List]):
    """访问根节点"""
    return root[0]


def get_left_child(root: List[List]):
    """访问左子树"""
    return root[1]


def get_right_child(root: List[List]):
    """访问右子树"""
    return root[2]


# 使用节点和引用表示二叉树
class BinaryTree:
    def __init__(self, root_val: Any):
        self._root = root_val
        self._left_child: BinaryTree = None
        self._right_child: BinaryTree = None

    def insert_left(self, new_val: Any):
        t = BinaryTree(new_val)
        t._left_child = self._left_child
        self._left_child = t

    def insert_right(self, new_val: Any):
        t = BinaryTree(new_val)
        t._right_child = self._right_child
        self._right_child = t

    def get_root_val(self):
        return self._root

    def get_left_child(self):
        return self._left_child

    def get_right_child(self):
        return self._right_child

    def set_root_val(self, root_val: Any):
        self._root = root_val


if __name__ == '__main__':
    t1 = binary_tree_by_list('a')
    print(t1)  # ['a', [], []]

    insert_left(t1, 'b')
    insert_right(t1, 'c')
    print(t1)  # ['a', ['b', [], []], ['c', [], []]]

    print(get_root_val(t1))  # a
    print(get_right_child(t1))  # ['c', [], []]
    print(get_left_child(t1))  # ['b', [], []]

    set_root_val(t1, "hello")
    print(t1)  # ['hello', ['b', [], []], ['c', [], []]]

    t2 = BinaryTree('a')
    print(t2.get_root_val())  # a

    t2.insert_left('b')
    t2.insert_right('c')
    print(t2.get_left_child().get_root_val())  # b
    print(t2.get_right_child().get_root_val())  # c

    t2.set_root_val("hello")
    print(t2.get_root_val())  # hello
