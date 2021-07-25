#!/user/bin/python
# -*-coding:UTF-8-*-


"""使用栈解决骑士周游问题：
问题描述：国际象棋中的骑士，行棋方式与中国象棋中的马相类似，走“日”字。
        现在的问题是，在国际象棋棋盘上为骑士找到一条路径，
        使之可以经过棋盘的每个格子恰好一次，并返回路径参数的表。
"""
import time
from typing import List, Tuple

DIRS = ((2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2))


def mark(board: List[List[int]], pos: Tuple[int, int], steps: int):
    board[pos[0]][pos[1]] = steps


def dismark(board: List[List[int]], pos: Tuple[int, int]):
    board[pos[0]][pos[1]] = 0


def passible(board: List[List[int]], pos: Tuple[int, int]) -> bool:
    if pos[0] < 0 or pos[0] > 7:
        return False
    if pos[1] < 0 or pos[1] > 7:
        return False
    return board[pos[0]][pos[1]] == 0


def print_path(board: List[List[int]]):
    for row in board:
        for column in row:
            print(column, end='\t')
        print()


def find_next(board: List[List[int]], current_knight: Tuple[int, int], st: List[Tuple[int, int]]) -> bool:
    """寻找下一步要探索的节点（即探索方向最少的节点）"""
    temp_lst = []

    for i in range(8):
        next_knight = (current_knight[0] + DIRS[i][0], current_knight[1] + DIRS[i][1])
        can_go = 0
        if passible(board, next_knight):
            for j in range(8):
                next_next_knight = (next_knight[0] + DIRS[j][0], next_knight[1] + DIRS[j][1])
                if passible(board, next_next_knight):
                    can_go += 1
            temp_lst.append([next_knight, can_go])

    if len(temp_lst) == 0:
        return False

    for next_knight, _ in sorted(temp_lst, key=lambda item: item[1], reverse=True):
        st.append(next_knight)

    return True


def knight_tour(board: List[List[int]], start: Tuple[int, int]):
    st: List[Tuple[int, int]] = []
    current_steps = 0
    st.append(start)

    while len(st) > 0:
        current_steps += 1
        current_knight = st.pop()
        mark(board, current_knight, current_steps)

        if current_steps == 64:
            break

        if find_next(board, current_knight, st):
            continue
        else:
            current_steps -= 1
            dismark(board, current_knight)


if __name__ == '__main__':
    b = [[0 for _ in range(8)] for _ in range(8)]

    knight_tour(board=b, start=(0, 4))

    print("Board: ")
    print_path(board=b)

# Board:
# 63	14	49	32	1	16	19	34
# 48	31	64	15	50	33	2	17
# 13	62	47	54	43	18	35	20
# 30	53	42	61	46	51	40	3
# 59	12	55	52	41	44	21	36
# 26	29	60	45	56	39	4	7
# 11	58	27	24	9	6	37	22
# 28	25	10	57	38	23	8	5
