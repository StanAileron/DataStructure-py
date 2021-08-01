#!/user/bin/python
# -*-coding:UTF-8-*-


"""Dijkstra算法：
1. 寻找带权重的图的最短路径。
2. 这是一个迭代算法，得出从一个顶点到其余所有顶点的最短路径，很接近于BFS算法的结果。
3. 具体实现上，在顶点Vertex类中增加成员 dist 用于记录从开始顶点到本顶点的最短带权路径长度（权重之和），算法对图中的每个顶点迭代一次。
4. 具体算法：
    - 顶点的访问次序有一个优先队列来控制，队列中作为优先级的是顶点的dist属性。
    - 最初只有开始顶点dist设为0，而其他所有顶点设为sys.maxsize（最大整数），全部加入队列。
    - 每次循环时队列中每个dist最小的顶点出队，根据它与它的邻接顶点的权重来修改它的邻接顶点的dist（如果）值，
      （如果计算出的值大于邻接顶点的dist值，则不行进行修改。）再将它的邻接顶点入队，这会引起堆重排。
    - 再次循环时，就会根据更新后的dist优先级再次出队。

这个算法保证，优先队列中队列首部的顶点的dist值一定是队列中所有顶点中最小的，即这个顶点到起始顶点的带权路径长度最短。
这样当迭代结束时，就找到了起始顶点到所有其他顶点最短带权路径。
"""
from queue import PriorityQueue

from graph import Graph


def dijkstra(g: Graph, start: str):
    pq = PriorityQueue()
    start = g.get_vertex(start)
    start.dist = 0

    for vertex in g:
        pq.put(vertex)

    while not pq.empty():
        vertex = pq.get()
        for connected_vertex in vertex.get_connections():
            if connected_vertex.color != "Black":
                new_dist = vertex.dist + vertex.get_weight(connected_vertex)
                if new_dist < connected_vertex.dist:
                    connected_vertex.pre_vertex = vertex
                    connected_vertex.dist = new_dist
                    # 优先队列重排（后续会修改这个垃圾实现，采用自己写的优先队列）
                    new_pq = PriorityQueue()
                    while not pq.empty():
                        v = pq.get()
                        if v.id == connected_vertex.id:
                            new_pq.put(connected_vertex)
                        else:
                            new_pq.put(v)

                    pq = new_pq

        vertex.color = "Black"


def build_graph() -> Graph:
    g = Graph()
    g.add_edge("U", "V", weight=2)
    g.add_edge("V", "U", weight=2)

    g.add_edge("U", "X", weight=1)
    g.add_edge("X", "U", weight=1)

    g.add_edge("X", "V", weight=2)
    g.add_edge("V", "X", weight=1)

    g.add_edge("V", "W", weight=3)
    g.add_edge("W", "V", weight=3)

    g.add_edge("U", "W", weight=5)
    g.add_edge("W", "U", weight=5)

    g.add_edge("X", "W", weight=3)
    g.add_edge("W", "X", weight=3)

    g.add_edge("X", "Y", weight=1)
    g.add_edge("Y", "X", weight=1)

    g.add_edge("W", "Y", weight=1)
    g.add_edge("Y", "W", weight=1)

    g.add_edge("Y", "Z", weight=1)
    g.add_edge("Z", "Y", weight=1)

    g.add_edge("W", "Z", weight=5)
    g.add_edge("Z", "W", weight=5)

    return g


def print_path(g: Graph, end: "str"):
    temp_lst = []

    x = g.get_vertex(end)
    y = x
    while y is not None:
        temp_lst.append(y.id)
        y = y.pre_vertex

    print(f"路径长度：{x.dist}", "-->".join(reversed(temp_lst)))


if __name__ == '__main__':
    bg = build_graph()

    dijkstra(bg, start="U")

    print_path(bg, "X")  # 路径长度：1 U-->X
    print_path(bg, "W")  # 路径长度：3 U-->X-->Y-->W
    print_path(bg, "Y")  # 路径长度：2 U-->X-->Y
    print_path(bg, "Z")  # 路径长度：3 U-->X-->Y-->Z
