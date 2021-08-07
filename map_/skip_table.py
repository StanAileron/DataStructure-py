#!/user/bin/python
# -*-coding:UTF-8-*-


"""利用跳表实现映射数据类型：
插入和查找的时间复杂度都是O(log n)。
"""
import random
from typing import Optional, Any


class HeaderNode:
    """头节点类"""

    def __init__(self):
        self._next: Optional[DataNode] = None
        self._down: Optional["HeaderNode"] = None

    @property
    def next(self) -> Optional["DataNode"]:
        return self._next

    @next.setter
    def next(self, new_next: Optional["DataNode"]):
        self._next = new_next

    @property
    def down(self) -> Optional["HeaderNode"]:
        return self._down

    @down.setter
    def down(self, new_down: Optional["HeaderNode"]):
        self._down = new_down


class DataNode:
    """数据节点类"""

    def __init__(self, key: Any, value: Any):
        self._key = key
        self._value = value
        self._next: Optional["DataNode"] = None
        self._down: Optional["DataNode"] = None

    @property
    def key(self) -> Any:
        return self._key

    @property
    def value(self) -> Any:
        return self._value

    @value.setter
    def value(self, new_value: Any):
        self._value = new_value

    @property
    def next(self) -> Optional["DataNode"]:
        return self._next

    @next.setter
    def next(self, new_next: Optional["DataNode"]):
        self._next = new_next

    @property
    def down(self) -> Optional["DataNode"]:
        return self._down

    @down.setter
    def down(self, new_down: Optional["DataNode"]):
        self._down = new_down


class SkipTable:
    """跳表"""

    def __init__(self):
        self._head: Optional[HeaderNode] = None

    def get(self, key: Any) -> Optional[Any]:
        """
        从顶层节点开始搜索，如果没有数据节点就下降到下一层。
        如果有数据节点，就比较数据节点的key与查找的key的大小：
            如果key < current.next.key，说明这一层没有我们要找的key（因为每一层是一个有序链表），就下降到下一层。
            如果key = current.next.key，就返回value。
            如果key > current.next.key，就向右边搜索，设置current = current.next
        """
        current = self._head

        while current is not None:
            if current.next is None:
                current = current.down

            else:
                if key == current.next.key:
                    return current.next.value
                elif key < current.next.key:
                    current = current.down
                else:
                    current = current.next

        return None

    def put(self, key: Any, value: Any) -> None:
        """
        1. 如果self._head is None，则说明跳表是空的：
            - 这时候我们首先构建一个头节点和一个数据节点。
            - 然后使用flip()函数模拟抛硬币，其返回值只有0或1。
            - 如果返回值为1，则不断地创建新的头节点和数据节点，向上“建塔”。
            - 建塔的过程中不断更新表头节点和顶层数据节点。
        2. 如果self._head is not None，则说明跳表不是空的：
            - 首先我们搜索key在跳表中的位置，这个过程与get()方法相似。
                - 如果current.next is None，说明这个我们要插入的数据位于这个节点的右边，因此我们把这个节点保存到栈中，然后下降到下一层。
                - 如果key < current.next.key，说明我们要插入的数据位于这个节点的右边和这个节点的下一个节点的左边，我们把这个节点保存到栈中，然后下降到下一层。
                - 如果 key == current.next.key，说明找到了这个key，直接更新value，退出函数即可。
                - 如果 key > current.next.key，那么就继续向右边搜索即可。
            - 搜索完毕，如果没有return出函数，那么栈中就保存了要插入的数据的位置的节点。
            - 使用flip()函数模拟抛硬币，其返回值只有0或1：（向上建塔）
            - 如果返回值为1：
                - 首先判断栈是否为空，若不为空，则弹出节点，然后构建新的数据节点，设置弹出节点和新建数据节点的关系、新建数据节点和下一层节点的关系。
                - 若栈为空，则说明已经到了塔的最顶层，这时与self._head is None 中的情况一致。
        """
        if self._head is None:
            self._head = HeaderNode()  # 表头节点
            temp = DataNode(key, value)  # 构建数据节点
            self._head.next = temp
            top = temp  # 当前顶层的数据节点
            while self._flip() == 1:
                """根据模拟抛硬币的点数来决定是否向上建塔"""
                new_head = HeaderNode()
                temp = DataNode(key, value)
                temp.down = top
                new_head.down = self._head

                self._head = new_head  # 更新表层节点
                top = temp  # 更新顶层数据节点

        else:
            tower_stack = []
            current = self._head
            while current is not None:
                if current.next is None:
                    tower_stack.append(current)
                    current = current.down
                elif key < current.next.key:
                    tower_stack.append(current)
                    current = current.down
                elif key == current.next.key:
                    current.next.value = value
                    return
                else:
                    current = current.next

            lowest_level = tower_stack.pop()
            temp = DataNode(key, value)
            lowest_level.next, temp.next = temp, lowest_level.next
            top = temp
            while self._flip() == 1:
                """根据模拟抛硬币的点数来决定是否向上建塔"""
                if len(tower_stack) > 0:
                    next_level = tower_stack.pop()
                    temp = DataNode(key, value)
                    temp.down = top
                    next_level.next, temp.next = temp, next_level.next

                    top = temp  # 更新顶层数据节点
                else:
                    new_head = HeaderNode()
                    temp = DataNode(key, value)
                    new_head.next, new_head.down = temp, self._head
                    temp.down = top

                    self._head = new_head
                    top = temp

    @staticmethod
    def _flip() -> int:
        """模拟抛硬币"""
        return random.randrange(2)

    def __getitem__(self, key: Any) -> Optional[Any]:
        return self.get(key)

    def __setitem__(self, key: Any, value: Any):
        self.put(key, value)


class Map:
    def __init__(self):
        self._collection = SkipTable()

    def put(self, key: Any, value: Any):
        self._collection.put(key, value)

    def get(self, key: Any) -> Any:
        self._collection.get(key)
