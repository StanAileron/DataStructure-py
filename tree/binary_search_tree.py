#!/user/bin/python
# -*-coding:UTF-8-*-


"""实现二叉搜索树
1. 每个节点大于其左子节点的数据，小于其右子节点的数据。
2. 每个节点一定大于其左子树的所有的数据，小于其右子树所有节点的数据。
3. 性能分析：
    （1）put方法：
        如果顺序插入时，key值的大小随机分布，则put方法最差性能为O(log[2, n])。
        如果顺序插入时，key值的从小到大或者从大到小分布，则put方法最差性能为O(n)。
    （2）get方法：与put()方法的性能分析一致。
    （3）delete方法：与put(0方法的性能分析一致
"""
from typing import Any, Optional


class TreeNode:
    def __init__(self, key: Any, val: Any, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None,
                 parent: Optional["TreeNode"] = None):
        self._key = key
        self._payload = val
        self._left_child = left
        self._right_child = right
        self._parent = parent
        self._balance_factor = 0

    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, key: Any):
        self._key = key

    @property
    def value(self):
        return self._payload

    @value.setter
    def value(self, value):
        self._payload = value

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, node: Optional["TreeNode"]):
        self._parent = node

    @property
    def left_child(self) -> Optional["TreeNode"]:
        return self._left_child

    @left_child.setter
    def left_child(self, node: Optional["TreeNode"]):
        self._left_child = node

    @property
    def right_child(self) -> Optional["TreeNode"]:
        return self._right_child

    @right_child.setter
    def right_child(self, node: Optional["TreeNode"]):
        self._right_child = node

    @property
    def balance_factor(self) -> int:
        return self._balance_factor

    @balance_factor.setter
    def balance_factor(self, new_factor: int):
        self._balance_factor = new_factor

    def is_left_child(self) -> bool:
        return self._parent is not None and self._parent._left_child == self

    def is_right_child(self) -> bool:
        return self._parent is not None and self._parent._right_child == self

    def is_root(self) -> bool:
        return self._parent is None

    def is_leaf(self) -> bool:
        return self._left_child is None and self._right_child is None

    def has_any_children(self) -> bool:
        return self._left_child is not None or self._right_child is not None

    def has_both_children(self) -> bool:
        return self._right_child is not None and self._left_child is not None

    def find_successor(self) -> "TreeNode":
        """寻找后继节点，即被删节点右子树中最小的那个。(关键方法)"""
        success: Optional["TreeNode"] = None

        # 第一种情况，该节点有右子节点，后继节点是右子树中最小的节点。
        if self.right_child is not None:
            success = self.right_child._find_min()
        else:
            # 注意：delete()方法中不会遇到下面的几种情况
            if self.parent is not None:
                # 第二种情况，该节点没有右子节点，并且其本身是父节点的左子节点，后继节点就是其父节点。
                if self.is_left_child():
                    success = self.parent
                # 第三种情况，该节点没有右子节点，并且其本身是父亲节点的右子节点，后继节点就是除本身外父节点的后继节点。
                else:
                    self.parent.right_child = None
                    success = self.parent.find_successor()
                    self.parent.right_child = self

        # success=None则说明，当前节点是根节点并且没有右子节点，后继节点就是它本身。
        return success

    def _find_min(self) -> "TreeNode":
        """寻找当前树中的最小节点"""
        current_node = self
        while current_node.left_child is not None:
            current_node = current_node.left_child
        return current_node

    def splice_out(self):
        """删除当前节点，delete()方法中：当前节点只可能是叶子节点或者有一个右子节点"""
        if self.is_leaf():
            if self.is_right_child():
                self._parent._right_child = None
            else:
                self._parent._left_child = None
        elif self.has_any_children():
            if self._right_child is not None:
                if self.is_left_child():
                    self._parent._left_child = self._right_child
                else:
                    self._parent._right_child = self._right_child

                self._right_child._parent = self._parent
            else:
                # 注意：delete()方法中不会遇到下面几种情况。
                if self.is_left_child():
                    self._parent._left_child = self._left_child
                else:
                    self._parent._right_child = self._left_child
                self._left_child._parent = self._parent

    def __iter__(self):
        if self:
            if self.left_child is not None:
                for elem in self.left_child:
                    yield elem

            yield self._key

            if self.right_child is not None:
                for elem in self._right_child:
                    yield elem

    # def replace_node_data(self, key: Any, value: Any, lc: Optional["TreeNode"] = None, rc: Optional["TreeNode"] =
    # None): self._key = key self._payload = value self._left_child = lc self._right_child = rc if self.left_child is
    # not None: self._left_child._parent = self if self.right_child is not None: self._right_child._parent = self


class BinarySearchTree:
    def __init__(self):
        self._root: Optional[TreeNode] = None
        self._size = 0

    def length(self) -> int:
        return self._size

    def put(self, key: Any, value: Any):
        if self._root is None:
            self._root = TreeNode(key, value)
        else:
            self._put(self._root, key, value)

    def _put(self, current_node: TreeNode, key: Any, value: Any):
        if key == current_node.key:
            current_node.value = value

        elif key < current_node.key:
            if current_node.left_child is None:
                current_node.left_child = TreeNode(key, value, parent=current_node)
                self._size += 1
            else:
                self._put(current_node.left_child, key, value)

        elif key > current_node.key:
            if current_node.right_child is None:
                current_node.right_child = TreeNode(key, value, parent=current_node)
                self._size += 1
            else:
                self._put(current_node.right_child, key, value)

    def get(self, key: Any) -> Optional[Any]:
        find_node = self._get(self._root, key)
        return None if find_node is None else find_node.value

    def _get(self, current_node: Optional[TreeNode], key) -> Optional[TreeNode]:
        if current_node is None:
            return None
        elif current_node.key == key:
            return current_node
        elif key < current_node.key:
            return self._get(current_node.left_child, key)
        elif key > current_node.key:
            return self._get(current_node.right_child, key)

    def delete(self, key: Any):
        find_node = self._get(self._root, key)
        if find_node is None:
            raise KeyError("the key not exist")

        self._remove(find_node)
        self._size -= 1

    def _remove(self, find_node: TreeNode):
        if find_node.is_leaf():
            if find_node.is_left_child():
                find_node.parent.left_child = None
            elif find_node.is_right_child():
                find_node.parent.right_child = None
            else:
                self._root = None

        elif find_node.has_both_children():
            success = find_node.find_successor()
            success.splice_out()
            find_node.key = success.key
            find_node.value = success.value

        elif find_node.left_child is not None:
            if not find_node.is_root():
                left_child, parent = find_node.left_child, find_node.parent
                left_child.parent = parent
                if find_node.is_left_child():
                    parent.left_child = left_child
                else:
                    parent.right_child = left_child
            else:
                left_child = find_node.left_child
                left_child.parent = None
                self._root = left_child

        elif find_node.right_child is not None:
            if not find_node.is_root():
                right_child, parent = find_node.right_child, find_node.parent
                right_child.parent = parent
                if find_node.is_right_child():
                    parent.right_child = right_child
                else:
                    parent.left_child = right_child
            else:
                right_child = find_node.right_child
                right_child.parent = None
                self._root = right_child

    def __setitem__(self, key: Any, value: Any):
        self.put(key, value)

    def __getitem__(self, key: Any) -> Optional[Any]:
        return self.get(key)

    def __delitem__(self, key: Any):
        self.delete(key)

    def __contains__(self, key: Any):
        return self.get(key) is not None

    def __iter__(self):
        return self._root.__iter__()

    def __len__(self):
        return self._size
