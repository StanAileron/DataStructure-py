#!/user/bin/python
# -*-coding:UTF-8-*-


"""实现哈希表(散列表)"""


class HashMap:
    def __init__(self):
        self._size = 11  # 散列表的长度
        self._slots = [None] * self._size  # 存放key的列表
        self._data = [None] * self._size  # 存放data的列表

    def put(self, key, data):
        hash_value = self._hash(key)
        if self._slots[hash_value] is None:
            self._slots[hash_value] = key
            self._data[hash_value] = data
        else:
            if self._slots[hash_value] == key:
                self._data[hash_value] = data
            else:
                next_slot = self._rehash(hash_value)
                while self._slots[next_slot] is not None and self._slots[next_slot] != key:
                    next_slot = self._rehash(next_slot)

                if self._slots[next_slot] is None:
                    self._slots[next_slot] = key
                    self._data[next_slot] = data
                else:
                    self._data[next_slot] = data  # 替换数据

    def get(self, key):
        start_slot = self._hash(key)
        if self._slots[start_slot] == key:
            return self._data[start_slot]
        else:
            next_slot = self._rehash(start_slot)
            while next_slot != start_slot:  # 如果和初始散列值相同，则说明找遍所有的槽都没有对应的键
                if self._slots[next_slot] == key:
                    return self._data[next_slot]
                next_slot = self._rehash(next_slot)
        return None

    def _hash(self, key):
        if isinstance(key, str):
            return self._hash_str(key)
        elif isinstance(key, int):
            return key % self._size
        else:
            pass

    def _hash_int(self, key):
        return key % self._size

    def _hash_str(self, key):
        all_weight = (1 + len(key)) * len(key) // 2
        sum_ = 0
        for pos in range(1, len(key) + 1):
            sum_ += sum_ + int(ord(key[pos]) * (pos / all_weight))

        return sum_ % self._size

    def _rehash(self, oldhash):
        return (oldhash + 3) % self._size

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.put(key, value)

    def __contains__(self, key):
        return self.get(key) is not None

    def __str__(self):
        str_lst = ["{ "]
        for i in range(len(self._slots)):
            if self._slots[i] is not None:
                if i == len(self._slots) - 1:
                    str_lst.append(f"{self._slots[i]}: {self._data[i]}")
                else:
                    str_lst.append(f"{self._slots[i]}: {self._data[i]}, ")
        str_lst.append(" }")
        return "".join(str_lst)


if __name__ == '__main__':
    hm = HashMap()
    hm[54] = "cat"
    hm[26] = "dog"
    hm[93] = "lion"
    hm[17] = "tiger"
    hm[77] = "bird"
    hm[31] = "cow"
    hm[44] = "goat"
    hm[55] = "pig"
    hm[20] = "chichen"

    print(hm)
    # { 77: bird, 55: pig, 44: goat, 26: dog, 93: lion, 17: tiger, 20: chichen, 31: cow, 54: cat }

    print(hm[54], hm[93], hm[31], hm[32])  # cat lion cow None

    print(32 in hm)  # False
    print(31 in hm)  # True
