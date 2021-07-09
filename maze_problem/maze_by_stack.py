#!/user/bin/python
# -*-coding:UTF-8-*-


"""使用栈解决迷宫问题"""
from typing import List

from stack.stack import Stack

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 东南西北


def mark(maze_: List[list], pos: tuple):
    """对已经探索的位置进行标记"""
    maze_[pos[0]][pos[1]] = 2


def possible(maze_: List[list], pos: tuple):
    """判断当前位置是否可行"""
    return maze_[pos[0]][pos[1]] == 0


def print_path(st: Stack):
    """输出路径"""
    while not st.is_empty():
        if st.length() == 1:
            print(st.pop()[0])
        else:
            print(st.pop()[0], end="<--")


def maze_solve(maze_: List[list], start: tuple, end: tuple):
    if start == end:
        return start

    st = Stack()
    mark(maze_, start)
    st.push((start, 0))
    while not st.is_empty():
        pos, i = st.pop()
        if i == 4:
            continue
        for item in range(i, 4):
            next_pos = (pos[0] + dirs[item][0], pos[1] + dirs[item][1])
            if next_pos == end:
                st.push((pos, 0))
                st.push((end, 0))
                print_path(st)
                return
            if possible(maze_, next_pos):
                st.push((pos, i + 1))
                mark(maze_, next_pos)
                st.push((next_pos, 0))
                break
    print("No path found")


if __name__ == '__main__':
    # 使用两层嵌套列表表示迷宫
    maze = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1],
        [1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    ]
    maze_solve(maze, (1, 1), (10, 12))
    # (10, 12)<--(9, 12)<--(8, 12)<--(7, 12)<--(6, 12)<--(5, 12)
    # <--(5, 11)<--(5, 10)<--(6, 10)<--(6, 9)<--(6, 8)<--(6, 7)
    # <--(6, 6)<--(6, 5)<--(6, 4)<--(6, 3)<--(7, 3)<--(7, 2)
    # <--(7, 1)<--(6, 1)<--(5, 1)<--(4, 1)<--(3, 1)<--(2, 1)<--(1, 1)
