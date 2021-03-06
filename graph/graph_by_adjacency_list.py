#!/user/bin/python
# -*-coding:UTF-8-*-

"""使用邻接表实现图数据结构"""
import sys
from typing import Any, Dict, Optional, KeysView


class Vertex:
    """表示顶点对象"""

    def __init__(self, key: Any):
        self._id = key

        self._color = "White"  # 标记当前顶点是否已被探查（White: 表示还没有进行探索，Gray：表示发现了这个顶点，Black：表示完成了对这个顶点的探索）
        self._distance = 0  # 记录当前顶点与起始顶点路径长度（不带权重）
        self._pre_vertex: Optional[Vertex] = None  # 记录当前顶点的前驱顶点

        self._steps = 0  # 记录当前顶点的对应的步数（用于骑士周游算法）

        self._dist = sys.maxsize  # 记录起始顶点到当前顶点的带权路径长度（用于Dijkstra算法）

        self._discovery = 0  # 记录在第几步访问到了这个顶点（用于带有通用dfs算法的图）
        self._finish = 0  # 记录在第几步完成了对这个顶点的探索（用于带有通用dfs算法的图）

        self._connected_to: Optional[Dict["Vertex", int]] = {}

    @property
    def id(self) -> Any:
        """获取顶点的id"""
        return self._id

    @property
    def color(self) -> str:
        return self._color

    @color.setter
    def color(self, new_color: str):
        self._color = new_color

    @property
    def distance(self) -> int:
        return self._distance

    @distance.setter
    def distance(self, new_distance: int):
        self._distance = new_distance

    @property
    def pre_vertex(self) -> "Vertex":
        return self._pre_vertex

    @pre_vertex.setter
    def pre_vertex(self, pre: "Vertex"):
        self._pre_vertex = pre

    @property
    def steps(self) -> int:
        return self._steps

    @steps.setter
    def steps(self, step: int):
        self._steps = step

    @property
    def discovery(self) -> int:
        return self._discovery

    @discovery.setter
    def discovery(self, step: int):
        self._discovery = step

    @property
    def finish(self) -> int:
        return self._finish

    @finish.setter
    def finish(self, step: int):
        self._finish = step

    @property
    def dist(self):
        return self._dist

    @dist.setter
    def dist(self, dist: int):
        self._dist = dist

    def add_neighbor(self, nbr: "Vertex", weight: int = 0):
        """建立当前顶点与顶点nbr的连接，并设置边的权重"""
        self._connected_to[nbr] = weight

    def get_connections(self) -> KeysView["Vertex"]:
        """获取与当前顶点相连接的所有顶点"""
        return self._connected_to.keys()

    def get_weight(self, nbr: "Vertex") -> int:
        """获取当前顶点与顶点nbr连接的边的权重"""
        return self._connected_to[nbr]

    def remove(self, v: "Vertex"):
        del self._connected_to[v]

    def __str__(self):
        return " ".join([str(self._id), "connected to:", str([x.id for x in self._connected_to])])

    def __lt__(self, other: "Vertex"):
        return self.dist < other.dist


class Graph:
    """表示图对象"""

    def __init__(self):
        self._vertex_list: Dict[Any, Vertex] = {}
        self._vertices_num = 0

    def add_vertex(self, key: Any) -> Vertex:
        """添加顶点"""
        self._vertices_num += 1
        new_vertex = Vertex(key)
        self._vertex_list[key] = new_vertex
        return new_vertex

    def get_vertex(self, key: Any) -> Optional[Vertex]:
        """获取顶点"""
        if key in self._vertex_list:
            return self._vertex_list[key]
        else:
            return None

    def add_edge(self, fr: Any, to: Any, weight: int = 0):
        """建立顶点fr与顶点to之间的连接"""
        if fr not in self._vertex_list:
            self.add_vertex(fr)
        if to not in self._vertex_list:
            self.add_vertex(to)
        self._vertex_list[fr].add_neighbor(self._vertex_list[to], weight)

    def get_vertices(self) -> KeysView[Any]:
        """获取所有的顶点名称"""
        return self._vertex_list.keys()

    def __contains__(self, key: Any):
        return key in self._vertex_list

    def __iter__(self):
        """返回所有的顶点对象"""
        return iter(self._vertex_list.values())


if __name__ == '__main__':
    g = Graph()
    for i in range(6):
        g.add_vertex(i)

    g.add_edge(0, 1, 5)
    g.add_edge(0, 5, 2)
    g.add_edge(1, 2, 4)
    g.add_edge(2, 3, 9)
    g.add_edge(3, 4, 7)
    g.add_edge(3, 5, 3)
    g.add_edge(4, 0, 1)
    g.add_edge(5, 4, 8)
    g.add_edge(5, 2, 1)

    for v in g:
        print(v)
        for w in v.get_connections():
            print(f"{v.id} ---> {w.id}")

    # 0 connected to: [1, 5]
    # 0 ---> 1
    # 0 ---> 5
    # 1 connected to: [2]
    # 1 ---> 2
    # 2 connected to: [3]
    # 2 ---> 3
    # 3 connected to: [4, 5]
    # 3 ---> 4
    # 3 ---> 5
    # 4 connected to: [0]
    # 4 ---> 0
    # 5 connected to: [4, 2]
    # 5 ---> 4
    # 5 ---> 2
