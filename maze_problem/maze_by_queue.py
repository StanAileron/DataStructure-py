#!/user/bin/python
# -*-coding:UTF-8-*-


"""使用队列解决迷宫问题"""
from typing import List

from queue_.queue_ import SQueue

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 东南西北


def mark(maze_: List[list], pos: tuple):
    """对已经探索的位置进行标记"""
    maze_[pos[0]][pos[1]] = 2


def possible(maze_: List[list], pos: tuple):
    """判断当前位置是否可行"""
    return maze_[pos[0]][pos[1]] == 0


def print_path(opposite: dict, start: tuple, end: tuple):
    print("found path: ")
    pos = end
    while True:
        print(f"{pos}<-- ", end="")
        if pos == start:
            return
        pos = opposite[pos]


def maze_solve(maze: List[list], start: tuple, end: tuple):
    if start == end:
        print("found path: ", start)
        return

    sq = SQueue()
    mark(maze, start)
    sq.enqueue(start)
    opposite = {}  # 记录路径之间的对应关系

    while not sq.is_empty():
        pos = sq.dequeue()
        if pos == end:
            print_path(opposite, start, end)
            return
        for i in range(4):
            next_pos = (pos[0] + dirs[i][0], pos[1] + dirs[i][1])
            if possible(maze, next_pos):
                mark(maze, next_pos)
                opposite[next_pos] = pos
                sq.enqueue(next_pos)

    print("Not found path")


if __name__ == "__main__":
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
    # found path:
    # (10, 12) < -- (9, 12) < -- (8, 12) < -- (7, 12) < -- (6, 12) < -- (5, 12) < -- (5, 11) < -- (5, 10) < -- (
    # 6, 10) < -- (6, 9) < -- (6, 8) < -- (6, 7) < -- (6, 6) < -- (6, 5) < -- (6, 4) < -- (6, 3) < -- (7, 3) < -- (
    # 7, 2) < -- (7, 1) < -- (6, 1) < -- (5, 1) < -- (4, 1) < -- (3, 1) < -- (2, 1) < -- (1, 1) < --
