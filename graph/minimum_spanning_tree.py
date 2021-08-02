#!/user/bin/python
# -*-coding:UTF-8-*-

"""最小权重生成树（minimum weight spanning tree）:
1. 生成树定义：拥有图中所有的顶点和最少数量的边，以保持连通的子图。
2. 最小生成树定义：图（G，E）的最小生成树T，定义为：包含所有顶点V，以及E的无圈子集(无循环图)，并且边权重之后最小。

3. 最小生成树的Prim算法：
    - 每步都沿着最小权重的边向前搜索。
    - 如果T还不是最小生成树，则反复做：找到一条最小权重的可以安全添加的边，将边添加到树T。
    - “可以安全添加的边”被定义为一端顶点在树中，另一端不在树中的边，以便保持树的无圈特性。
"""

from queue import PriorityQueue

from graph import Graph


def prim(g: Graph, start: str):
    pq = PriorityQueue()
    start = g.get_vertex(start)
    start.dist = 0

    for vertex in g:
        pq.put(vertex)

    while not pq.empty():
        vertex = pq.get()

        # 循环完毕后就找到了权重最小的边，这条边的不在树中的那一端顶点会排在优先队列队首，
        # 这样下一次循环时，这条权重最小的边就会被添加到树中。
        for connected_vertex in vertex.get_connections():
            new_cost = vertex.get_weight(connected_vertex)
            # 队列外的顶点在最小生成树中，“可以安全添加的边”一端顶点在树中，另一端不在树中，
            # 因此要首先判断顶点是否在队列中（即不在树中），判断这是否是一条“安全的边”。
            # 同时为了从最小权重的边进行探索，要判断 new_cost 是否小于 connected.dist，循环完毕后就找到了找到权重最小的安全的边。
            # 注意：这里的dist存储边的权重大小。
            if connected_vertex in pq and new_cost < connected_vertex.dist:
                connected_vertex.pre_vertex = vertex
                connected_vertex.dist = new_cost
                # 优先队列重排（后续会修改这个垃圾实现，采用自己写的优先队列）
                # 保证权重最小的边的顶点在优先队列队首，这样下一次循环时这条边就会被添加到最小生成树中。
                new_pq = PriorityQueue()
                while not pq.empty():
                    v = pq.get()
                    if v.id == connected_vertex.id:
                        new_pq.put(connected_vertex)
                    else:
                        new_pq.put(v)

                pq = new_pq


def build_graph() -> Graph:
    g = Graph()
    g.add_edge("A", "B", weight=2)
    g.add_edge("B", "a", weight=2)

    g.add_edge("A", "C", weight=3)
    g.add_edge("C", "A", weight=3)

    g.add_edge("B", "C", weight=1)
    g.add_edge("C", "B", weight=1)

    g.add_edge("B", "D", weight=1)
    g.add_edge("D", "B", weight=1)

    g.add_edge("B", "E", weight=4)
    g.add_edge("E", "B", weight=4)

    g.add_edge("C", "F", weight=5)
    g.add_edge("F", "C", weight=5)

    g.add_edge("D", "E", weight=1)
    g.add_edge("E", "D", weight=1)

    g.add_edge("E", "F", weight=1)
    g.add_edge("F", "E", weight=1)

    g.add_edge("F", "G", weight=1)
    g.add_edge("G", "F", weight=1)

    return g


def print_path(g: Graph, end: "str"):
    temp_lst = []

    x = g.get_vertex(end)
    y = x
    while y is not None:
        temp_lst.append(y.id)
        y = y.pre_vertex

    print(f"路径长度：{x.dist}", "-->".join(reversed(temp_lst)))
