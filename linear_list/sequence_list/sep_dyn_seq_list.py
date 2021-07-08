#!/user/bin/python
# -*-coding:UTF-8-*-

"""分离式动态顺序表"""
import random

EXPANSION_MULTIPLE = 1.5  # 当表满时，扩张的倍数


class PList(object):
    def __init__(self, *args):
        self._max = 4  # 最大元素个数
        self._num = 0  # 当前元素个数
        self._list = [None] * self._max
        self._initialize(*args)

    def _initialize(self, *args):
        """初始化表"""
        if args:
            self._max = int(len(args) * EXPANSION_MULTIPLE)
            self._num = len(args)
            self._list = [args[i_] if i_ < self._num else None for i_ in range(self._max)]

    def is_empty(self):
        """判断表是否为空"""
        return self._num != 0

    def length(self):
        """返回表当前元素的个数"""
        return self._num

    def prepend(self, elem):
        """将elem元素插入到表首"""
        num = self._num

        if self._num < self._max:
            while num > 0:
                self._list[num] = self._list[num - 1]
                num -= 1
            self._list[0] = elem
        else:
            self._max = int(self._max * EXPANSION_MULTIPLE)
            new_list = [None] * self._max
            while num > 0:
                new_list[num] = self._list[num - 1]
                num -= 1
            new_list[0] = elem
            self._list = new_list

        self._num += 1

    def append(self, elem):
        """将elem元素插入到表尾"""
        if self._num == self._max:
            self._max = int(self._max * EXPANSION_MULTIPLE)
            new_list = [None] * self._max
            for i in range(self._num):
                new_list[i] = self._list[i]
            self._list = new_list

        self._list[self._num] = elem
        self._num += 1

    def insert(self, elem, index):
        """将元素elem插入到index位置"""
        if index < 0:
            raise IndexError("index must greater than or equal to 0")

        num = self._num
        if self._num < self._max:
            while num > index:
                self._list[num] = self._list[num - 1]
                num -= 1
        else:
            self._max = int(self._max * EXPANSION_MULTIPLE)
            new_list = [None] * self._max
            for i in range(index):
                new_list[i] = self._list[i]
            while num > index:
                new_list[num] = self._list[num - 1]
                num -= 1

        self._list[index] = elem
        self._num += 1

    def del_first(self):
        """删除表首元素"""
        if self._num == 0:
            raise ValueError("list is null")

        del_item = self._list[0]
        for i in range(self._num - 1):
            self._list[i] = self._list[i + 1]

        self._num -= 1
        return del_item

    def del_last(self):
        """删除表尾元素"""
        if self._num == 0:
            raise ValueError("list is null")

        del_item = self._list[self._num - 1]

        self._num -= 1
        return del_item

    def pop(self, index):
        """删除指定位置的元素"""
        if self._num == 0:
            raise ValueError("list is null")
        if index < 0 or index >= self._num:
            raise IndexError("index error")

        del_item = self._list[index]

        for i in range(index, self._num):
            self._list[i] = self._list[i + 1]

        self._num -= 1
        return del_item

    def search(self, elem):
        """搜索元素elem在表中的第一次出现的位置"""
        for i in range(self._num):
            if elem == self._list[i]:
                return i
        return -1

    def clear(self):
        """清空列表"""
        self._num = 0
        self._max = 4

    def reverse(self):
        """反转列表"""
        for i in range(self._num // 2):
            temp = self._list[i]
            self._list[i] = self._list[self._num - i - 1]
            self._list[self._num - i - 1] = temp

    def sort(self):
        """插入排序"""
        if self._num <= 1:
            return
        # j = 1
        # while j != self.length():
        #     i_ = 0
        #     x = self._list[j]
        #     while i_ != j and self._list[i_] <= self._list[j]:
        #         i_ += 1
        #     while i_ != j:
        #         y = self._list[i]
        #         self._list[i] = x
        #         x = y
        #         i_ += 1
        #     self._list[j] = x
        #     j += 1

        # 更好的实现
        for j in range(1, self.length()):
            i_ = j - 1
            while i_ >= 0:
                if self._list[i_] > self._list[j]:
                    # 如果list[i] > list[j] 则一直向前交换，目的是把list[j]插入到合适的位置
                    self._list[i_], self._list[j] = self._list[j], self._list[i_]
                    i_ -= 1
                    j -= 1
                else:
                    break

    def __setitem__(self, key, value):
        if key >= self._num or key < 0:
            raise IndexError("index error")
        self._list[key] = value

    def __getitem__(self, item):
        if item >= self._num or item < 0:
            raise IndexError("index error")
        return self._list[item]

    def __getattr__(self, item):
        return self._list[item]

    def __len__(self):
        return self._num

    def __contains__(self, item):
        for i in range(self._num):
            if self._list[i] == item:
                return True
        return False

    def __str__(self):
        return str(self._list[0:self._num])


lst = PList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print(lst.search(4))  # 3

lst.reverse()
print(lst)  # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
lst.reverse()
print(lst)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lst.prepend(0)
print(lst.length())  # 11
print(lst)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lst.append(11)
print(lst.length())  # 12
print(lst)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

print(lst.del_first())  # 0
print(lst.length())  # 11
print(lst)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

print(lst.del_last())  # 11
print(lst.length())  # 10
print(lst)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lst.insert(2.5, 2)
print(lst.length())  # 11
print(lst)  # [1, 2, 2.5, 3, 4, 5, 6, 7, 8, 9, 10]

print(lst.pop(2))  # 2.5
print(lst.length())  # 10
print(lst)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in range(11, 17):
    lst.append(i)
print(lst.length())  # 16
print(lst)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

for i in range(0, -7, -1):
    lst.prepend(i)
print(lst.length())  # 23
print(lst)  # [-6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

lst.clear()
for i in range(10):
    lst.append(random.randint(0, i))
lst.sort()
print(lst)  # [0, 0, 2, 2, 2, 3, 3, 3, 3, 4]
