#!/user/bin/python
# -*-coding:UTF-8-*-


# noinspection SpellCheckingInspection
"""强连通分支：
1. 强连通分支：
    将C定义为图G的一个子集，C中的任意两个顶点v, w之间都有路径来回，即(v, w)(w, v)都是C的路径，
    而且C是具有这样性质的最大子集。

2. 强连通分支算法：在图中发现高度聚集节点群的算法，被称为强连通分支(Strongly Connected Components)算法。

3. 转置图：一个有向图的转置 G^T，定义为将图G的所有边的顶点交换次序，如将(v, w) 转换为 (w, v)，
   图和转置图在强连通分支的数量和划分上，是相同的。

4. 强连通分支算法：Kosaraju算法：
    - 对图 G 调用DFS算法，为每个顶点计算“结束时间”。
    - 对图 G 进行转置，得到 G^T。
    - 再次对 G^T 调用DFS算法，但在dfs函数中，对每个顶点的搜索循环里，要以顶点的“结束时间”倒序的顺序来搜索。
    - 深度优先森林中的每一棵树就是一个强连通分支。

5. 其他常用强连通分支算法：
    - Tarijan 算法。
    - Gabow 算法，这个是对Tarijan的改进。
"""
from graph import DFSGraph


class DFSGraphK(DFSGraph):
    def __init__(self):
        super(DFSGraphK, self).__init__()

    def dfs(self):
        for vertex in self:
            vertex.color = "White"
            vertex.pre_vertex = None

        # 如果有未包括的顶点则建立森林
        vertex_lst = list(self)
        for vertex in sorted(vertex_lst, key=lambda x: x.finish, reverse=True):
            if vertex.color == "White":
                self.dfs_visit(vertex)


def kosaraju(g: DFSGraphK):
    g.dfs()

    # 保存已经删除了的顶点对象之间的连接关系，如vertex: [connected_vertex1, connexted_vertex2]
    has_transport = {}

    # 对图进行转置
    for vertex in g:
        connections = list(vertex.get_connections())
        # 遍历连接的所有顶点
        for connected_vertex in connections:
            # 如果vertex在has_transport[connected_vertex]中，
            # 说明已经将connected_vertex ---> vertex 转置为 vertex ---> connected_vertex，此时不能再转置。
            if has_transport.get(connected_vertex) is None or vertex not in has_transport[connected_vertex]:
                vertex.remove(connected_vertex)
                connected_vertex.add_neighbor(vertex)

                if has_transport.get(vertex):
                    has_transport[vertex].append(connected_vertex)
                else:
                    has_transport[vertex] = [connected_vertex]

    g.dfs()


if __name__ == '__main__':
    g_ = DFSGraphK()
    g_.add_edge("A", "B")
    g_.add_edge("B", "C")
    g_.add_edge("B", "E")
    g_.add_edge("C", "F")
    g_.add_edge("D", "B")
    g_.add_edge("D", "G")
    g_.add_edge("E", "D")
    g_.add_edge("E", "A")
    g_.add_edge("F", "H")
    g_.add_edge("G", "E")
    g_.add_edge("H", "I")
    g_.add_edge("I", "F")

    print("转置前的图：")
    for v in g_:
        print(v)

    kosaraju(g_)

    v_lst = list(g_)
    print("\n转置后的图：")
    for v in v_lst:
        print(v)

    tree = [v.id for v in v_lst if v.pre_vertex is None]

    print("\n强连通分支的起始顶点：")
    print(", ".join(tree))

# 转置前的图：
# A connected to: ['B']
# B connected to: ['C', 'E']
# C connected to: ['F']
# E connected to: ['D', 'A']
# F connected to: ['H']
# D connected to: ['B', 'G']
# G connected to: ['E']
# H connected to: ['I']
# I connected to: ['F']
#
# 转置后的图：
# A connected to: ['E']
# B connected to: ['A', 'D']
# C connected to: ['B']
# E connected to: ['B', 'G']
# F connected to: ['C', 'I']
# D connected to: ['E']
# G connected to: ['D']
# H connected to: ['F']
# I connected to: ['H']
#
# 强连通分支的起始顶点：
# A, C, F
