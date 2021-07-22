#!/user/bin/python
# -*-coding:UTF-8-*-


"""AVL树：
1. 每个节点附加一个平衡因子参数，其值等于height(左子树)-height(右子树)。
2. 如果平衡因子>0，称之为左倾，平衡因子<0，称之为右倾。
3. AVL树在插入元素/删除元素是要保持二叉树处于平衡状态：即每个节点的|平衡因子参数| <= 1。
4. AVL树的搜索时间复杂度在最坏的情况下为O(log n)。
"""
from typing import Any

from tree.binary_search_tree import BinarySearchTree, TreeNode


class AVLTree(BinarySearchTree):
    def __init__(self):
        super(AVLTree, self).__init__()

    def _put(self, current_node: TreeNode, key: Any, value: Any):
        if key == current_node.key:
            current_node.key = key

        elif key < current_node.key:
            if current_node.left_child is not None:
                self._put(current_node.left_child, key, value)
            else:
                current_node.left_child = TreeNode(key, value, parent=current_node)
                self._update_balance(current_node.left_child)

        elif key > current_node.key:
            if current_node.right_child is not None:
                self._put(current_node.right_child, key, value)
            else:
                current_node.right_child = TreeNode(key, value, parent=current_node)
                self._update_balance(current_node.right_child)

    def _update_balance(self, current_node: TreeNode):
        # 如果当前节点不平衡，则进行再平衡，不需要更新父节点。
        if current_node.balance_factor > 1 or current_node.balance_factor < -1:
            self._re_balance(current_node)
            return

        # 如果当前节点是平衡的，则调节父节点的平衡因子
        parent = current_node.parent
        if current_node.is_left_child():
            parent.balance_factor += 1
        else:
            parent.balance_factor -= 1

        if not parent.is_root() and parent.balance_factor != 0:
            self._update_balance(current_node.parent)

    def _re_balance(self, current_node: TreeNode):
        # 重新平衡的示意图参见：rotate.md

        # 右重需要左旋
        if current_node.balance_factor < 0:
            # 右子节点左重需要先右旋
            if current_node.right_child.balance_factor > 0:
                self._rotate_right(current_node.right_child)
                self._rotate_left(current_node)
            else:
                self._rotate_left(current_node)
        # 左重需要右旋
        elif current_node.balance_factor > 0:
            # 左子节点右重需要先左旋
            if current_node.left_child.balance_factor < 0:
                self._rotate_left(current_node.left_child)
                self._rotate_right(current_node)
            else:
                self._rotate_right(current_node)

    def _rotate_left(self, current_node: TreeNode):
        """左旋"""
        new_root = current_node.right_child
        current_node.right_child = new_root.left_child
        if new_root.left_child is not None:
            new_root.left_child.parent = current_node

        if current_node.is_root():
            self._root = new_root
            new_root.parent = None
        else:
            if current_node.is_left_child():
                current_node.parent.left_child = new_root
            else:
                current_node.parent.right_child = new_root

        new_root.left_child, current_node.parent = current_node, new_root

        # 重点：更新平衡因子
        current_node.balance_factor = current_node.balance_factor + 1 - min(new_root.balance_factor, 0)
        new_root.balance_factor = new_root.balance_factor + 1 + max(current_node.balance_factor, 0)

    def _rotate_right(self, current_node: TreeNode):
        """右旋"""
        new_root = current_node.left_child
        current_node.left_child = new_root.right_child
        if new_root.right_child is not None:
            new_root.right_child.parent = current_node

        if current_node.is_root():
            self._root = new_root
            new_root.parent = None
        else:
            if current_node.is_left_child():
                current_node.parent.left_child = new_root
            else:
                current_node.parent.right_child = new_root

        new_root.right_child, current_node.parent = current_node, new_root

        # 重点：更新平衡因子
        current_node.balance_factor = current_node.balance_factor - 1 - max(0, new_root.balance_factor)
        new_root.balance_factor = new_root.balance_factor - 1 + min(0, current_node.balance_factor)