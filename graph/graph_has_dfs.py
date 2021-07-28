#!/user/bin/python
# -*-coding:UTF-8-*-


"""带有通用DFS算法的图
1. 一般的深度优先搜索目标是在图上尽量深的搜索，连接尽量多的顶点，必要时可以进行分支（创建了树）。
    有时深度优先搜索会创建多棵树，称为“深度优先森林”。

2. 深度优先搜索同样要用到顶点的“前驱”属性，来构建树或森林。
   另外要设置“发现时间”和“结束时间”属性：
        - 前者表示第几步访问到了这个顶点（设置灰色）
        - 后者表示在第几步完成了此顶点的探索（设置黑色）
"""
from graph import Graph, Vertex


class DFSGraph(Graph):
    def __init__(self):
        super(DFSGraph, self).__init__()
        self._time = 0  # 记录当前搜索的步数

    def dfs(self):
        # 颜色初始化
        for vertex in self:
            vertex.color = "White"
            vertex.pre_vertex = None

        # 如果有未包括的顶点则建立森林
        for vertex in self:
            if vertex.color == "White":
                self.dfs_visit(vertex)

    def dfs_visit(self, start_vertex: Vertex):
        start_vertex.color = "Gray"
        self._time += 1  # 当前搜索的步数
        start_vertex.discovery = self._time

        for next_vertex in start_vertex.get_connections():
            if next_vertex.color == "White":
                # 深度优先递归访问
                next_vertex.pre_vertex = start_vertex
                self.dfs_visit(next_vertex)

        start_vertex.color = "Black"
        self._time += 1
        start_vertex.finish = self._time
