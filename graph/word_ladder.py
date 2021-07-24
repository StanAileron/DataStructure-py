#!/user/bin/python
# -*-coding:UTF-8-*-

"""使用图解决词梯问题:
1. 问题描述：
    在给定的一堆单词中，将起始单词例如 FOOL 转换为 目标单词 SAGE，每次只能替换一个字母，
且每一步的结果都必须是一个单词，且这个单词必须存在给定的单词中。
2. 目标输出
    找到从起始单词到目标单词的最短路径。
"""

from queue import Queue
from typing import Dict, List

from graph import Graph


def build_graph(word_file: str) -> Graph:
    """构建单词关系图，示例图参见：单词关系图.jpg"""
    d: Dict[str, List[str]] = {}
    g = Graph()
    fp = open(word_file, 'r')

    # 创建词桶
    for line in fp:
        word = line[:-1]
        for i in range(len(word)):
            bucket = word[:i] + '_' + word[i + 1:]
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket] = [word]

    fp.close()

    # 为同一个词桶中的单词添加顶点和边
    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 != word2:
                    g.add_edge(word1, word2)

    return g


def bfs(g: Graph, start: str):
    """宽度优先搜索(时间复杂度：O(V + E))，搜索过程参见示例图：词梯问题的宽度优先搜索.jpg"""
    start = g.get_vertex(start)
    start.color = "Gray"
    q = Queue()
    q.put(start)

    while not q.empty():
        current_vertex = q.get()

        # 遍历所有相邻顶点
        for nbr in current_vertex.get_connections():
            # 颜色为白色，说明这个顶点还没有被发现
            if nbr.color == "White":
                nbr.color = "Gray"
                nbr.distance = current_vertex.distance + 1
                nbr.pre_vertex = current_vertex
                q.put(nbr)

        # 探索完毕，标记为黑色
        current_vertex.color = "Black"


def traverse(g: Graph, target: str):
    y = g.get_vertex(target)
    if y.pre_vertex is None:
        print("没有找到路径！！！")
        return

    print(f"路径长度为：{y.distance}, 具体路径：")
    x = y
    vertex_lst = []
    while x is not None:
        vertex_lst.append(x.id)
        x = x.pre_vertex

    print("-->".join(reversed(vertex_lst)))


if __name__ == '__main__':
    word_graph = build_graph("four_letter_words.txt")
    bfs(word_graph, "fool")
    traverse(word_graph, "sage")

# 路径长度为：6, 具体路径：
# fool-->pool-->poll-->pall-->pale-->sale-->sage
