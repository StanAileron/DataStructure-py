#!/user/bin/python
# -*-coding:UTF-8-*-


"""使用图解决骑士周游问题：
问题描述：国际象棋中的骑士，行棋方式与中国象棋中的马相类似，走“日”字。
        现在的问题是，在国际象棋棋盘上为骑士找到一条路径，
        使之可以经过棋盘的每个格子恰好一次，并返回路径参数的表。
"""
from typing import List, Tuple

from graph import Graph, Vertex

DIRS = ((2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2))


def in_board(pos: Tuple[int, int]) -> bool:
    """判断pos位置是否在棋盘中"""
    if pos[0] < 0 or pos[0] > 7:
        return False

    if pos[1] < 0 or pos[1] > 7:
        return False

    return True


def possible(v: Vertex) -> bool:
    """判断顶点v对应的位置是否没有被走过"""
    return v.steps == 0


def mark(v: Vertex, current_steps: int):
    """标记顶点v对应的位置的步数"""
    v.steps = current_steps


def dis_mark(v: Vertex):
    """重置顶点v对应的位置的步数"""
    v.steps = 0


def print_path(g: Graph):
    """打印棋盘"""
    for i in range(8):
        for j in range(8):
            v = g.get_vertex((i, j))
            print(v.steps, end='\t\t')
        print()


def build_graph() -> Graph:
    """构建位置图，令8 * 8 棋盘的每个位置与其可形成日字走向的其他位置建立边，
       顶点对象的key值使用棋盘的位置坐标（i, j）。
    """
    g = Graph()
    for i in range(8):
        for j in range(8):
            pos = (i, j)
            for item in DIRS:
                next_pos = (pos[0] + item[0], pos[1] + item[1])
                if in_board(next_pos):
                    g.add_edge(pos, next_pos)

    return g


def find_next(current_v: Vertex, st: List[Vertex]) -> bool:
    """寻找深度优先搜索中下一步要探索的顶点（这个顶点的可探索方向的数量最少）"""

    # 保存下一步可以探索的顶点和从这个顶点出发可以探索的方向的数量
    temp_lst = []

    for next_knight in current_v.get_connections():
        if possible(next_knight):
            can_go = 0
            for next_next_knight in next_knight.get_connections():
                if possible(next_next_knight):
                    can_go += 1
            temp_lst.append([next_knight, can_go])

    # 如果为空，则说明找不到下一步可以探索的顶点，返回False
    if len(temp_lst) == 0:
        return False

    # 对temp_lst从大到小排序，保证最后一个入栈的顶点是从这个顶点出发可探索方向数量最少的顶点，
    # 这样，下一次循环中弹出的顶点就是我们想要探索的顶点了。
    for knight, _ in sorted(temp_lst, key=lambda x: x[1], reverse=True):
        st.append(knight)

    return True


def dfs(g: Graph, start: Tuple[int, int]):
    """深度优先搜索"""
    st = [g.get_vertex(start)]

    current_steps = 0
    while len(st) > 0:
        current_steps += 1
        current_v = st.pop()  # 当前的顶点对象，其含有在棋盘中的位置(i, j)和这个位置对应的步数step。
        mark(current_v, current_steps)

        if current_steps == 64:
            break

        if find_next(current_v, st):
            continue
        else:
            # 如果为False，则说明从当前顶点出发无法找到下一步可探索的顶点，
            # 因此减少步数，重置当前顶点对应位置的步数，然后回溯到上一个顶点继续探索。
            current_steps -= 1
            dis_mark(current_v)


def get_sort_connections(current_v: Vertex) -> List[Vertex]:
    v_lst = []
    for next_v in current_v.get_connections():
        if possible(next_v):
            can_go = 0
            for next_next_v in next_v.get_connections():
                if possible(next_next_v):
                    can_go += 1
            v_lst.append([next_v, can_go])

    v_lst.sort(key=lambda x: x[1])
    return [v[0] for v in v_lst]


def dfs_recursion(current_v: Vertex, current_steps: int, limit: int) -> bool:
    current_steps += 1
    mark(current_v, current_steps)

    if current_steps == limit:
        return True

    for next_v in get_sort_connections(current_v):
        if dfs_recursion(next_v, current_steps, limit):
            return True

    current_steps -= 1
    dis_mark(current_v)
    return False


if __name__ == '__main__':
    pos_graph = build_graph()
    dfs(g=pos_graph, start=(0, 4))
    print_path(pos_graph)

    print('\n')

    pos_graph2 = build_graph()
    dfs_recursion(pos_graph2.get_vertex((0, 4)), 0, 64)
    print_path(pos_graph2)

# 63		14		49		32		1		16		19		34
# 48		31		64		15		50		33		2		17
# 13		62		47		54		43		18		35		20
# 30		53		42		61		46		51		40		3
# 59		12		55		52		41		44		21		36
# 26		29		60		45		56		39		4		7
# 11		58		27		24		9		6		37		22
# 28		25		10		57		38		23		8		5
#
#
# 11		14		29		56		1		16		19		44
# 30		63		12		15		28		45		2		17
# 13		10		55		48		57		18		43		20
# 64		31		62		35		54		27		46		3
# 9		    36		49		58		47		42		21		26
# 32		61		34		53		24		51		4		41
# 37		8		59		50		39		6		25		22
# 60		33		38		7		52		23		40		5
