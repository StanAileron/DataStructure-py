#!/user/bin/python
# -*-coding:UTF-8-*-

"""使用邻接表实现图数据结构"""
from typing import Any, Dict, Optional, KeysView


class Vertex:
    """表示顶点对象"""

    def __init__(self, key: Any):
        self._id = key
        self._connected_to: Optional[Dict["Vertex", int]] = {}

    @property
    def id(self) -> Any:
        """获取顶点的id"""
        return self._id

    def add_neighbor(self, nbr: "Vertex", weight: int = 0):
        """建立当前顶点与顶点nbr的连接，并设置边的权重"""
        self._connected_to[nbr] = weight

    def get_connections(self) -> KeysView["Vertex"]:
        """获取与当前顶点相连接的所有顶点"""
        return self._connected_to.keys()

    def get_weight(self, nbr: "Vertex") -> int:
        """获取当前顶点与顶点nbr连接的边的权重"""
        return self._connected_to[nbr]

    def __str__(self):
        return " ".join([str(self._id), "connected to:", str([x.id for x in self._connected_to])])


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



