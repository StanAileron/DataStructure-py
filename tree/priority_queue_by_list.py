#!/user/bin/python
# -*-coding:UTF-8-*-


"""使用列表实现优先队列，
优先队列的特点是存入队列中的每项数据都另外附有一个值，表示这项的优先程度，称为优先级。
优先队列保证，任何时刻出队或访问的都是这个结构中优先级最高的一项。
"""


class PrioQueueError(ValueError):
    pass


class PrioQueue:
    def __init__(self, elist=[]):
        self._elems = list(elist)
        self._elems.sort(reverse=True)

    def is_empty(self):
        return self._elems == []

    def enqueue(self, elem):
        has_insert = False
        for idx, item in enumerate(self._elems):
            if elem >= item:
                self._elems.insert(idx, elem)
                has_insert = True
                break
        if not has_insert:
            self._elems.append(elem)

    def dequeue(self):
        if self.is_empty():
            raise PrioQueueError("the queue is null")
        return self._elems.pop()

    def peek(self):
        if self.is_empty():
            raise PrioQueueError("the queue is null")
        return self._elems[-1]

    def __str__(self):
        return str(self._elems)


if __name__ == '__main__':
    pq = PrioQueue([1, 4, 3, 6, 3, 6, 5, 2])

    print(pq)  # [6, 6, 5, 4, 3, 3, 2, 1]
    print(pq.peek())  # 1
    print(pq.dequeue())  # 1
    print(pq)  # [6, 6, 5, 4, 3, 3, 2]

    pq.enqueue(1)
    print(pq)  # [6, 6, 5, 4, 3, 3, 2, 1]
    print(pq.peek())  # 1
