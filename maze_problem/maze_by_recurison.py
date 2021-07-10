#!/user/bin/python
# -*-coding:UTF-8-*-

"""使用递归解决迷宫问题"""
from typing import List

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 东南西北


def mark(maze_: List[list], pos: tuple):
    """对已经探索的位置进行标记"""
    maze_[pos[0]][pos[1]] = 2


def possible(maze_: List[list], pos: tuple):
    """判断当前位置是否可行"""
    return maze_[pos[0]][pos[1]] == 0


def maze_solve(maze_: List[list], start: tuple, end: tuple):
    if start == end:
        print(start, end="<--")
        return True

    mark(maze_, start)
    for i in range(4):
        next_pos = (start[0] + dirs[i][0], start[1] + dirs[i][1])
        if possible(maze_, next_pos):
            mark(maze_, next_pos)
            if maze_solve(maze_, next_pos, end):
                print(start, end="<--")
                return True


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
    # (10, 12) < --(9, 12) < --(8, 12) < --(7, 12) < --(6, 12) < --(5, 12) < --(5, 11) < --(5, 10)
    # < --(6, 10) < --(6, 9) < --(6, 8) < --(6, 7) < --(6, 6) < --(6, 5) < --(6, 4) < --(6, 3)
    # < --(7, 3) < --(7, 2) < --(7, 1) < --(6, 1) < --(5, 1) < --(4, 1) < --(3, 1) < --(2, 1) < --(1, 1) < --
