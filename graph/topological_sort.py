#!/user/bin/python
# -*-coding:UTF-8-*-


"""拓扑排序：
1. 从工作流程图得到工作次序排序的算法，称为 “拓扑排序”。
2. 拓扑排序处理一个DAG（有向无环图），输出顶点的线性序列。
3. 拓扑排序应用在 依赖事件 的排期上，还可以用在项目管理、数据库查询优化和矩阵乘法的次序优化上。

拓扑排序可以采用DFS很好地实现：
    - 将工作流程建立为图，工作项是节点，依赖关系是有向边。
    - 工作流程图必须是一个 DAG 图，否则会产生循环依赖。
    - 对 DAG 图调用 DFS 算法，以得到每个顶点的 “结束事件”。
    - 根据每个顶点的 “结束时间” 从大到小排序输出这个次序下的顶点列表。
"""
from typing import List

from graph import DFSGraph


def build_graph() -> DFSGraph:
    """构建工作事件依赖图"""
    g = DFSGraph()
    g.add_edge("3/4 cup milk", "1 cup mix")
    g.add_edge("1 egg", "1 cup mix")
    g.add_edge("1 Tbl Oil", "1 cup mix")
    g.add_edge("1 cup mix", "pour 1/4 cup")
    g.add_edge("1 cup mix", "heat syrup")
    g.add_edge("heat syrup", "eat")
    g.add_edge("heat griddle", "pour 1/4 cup")
    g.add_edge("pour 1/4 cup", "turn when bubbly")
    g.add_edge("turn when bubbly", "eat")

    return g


def topological_sort(g: DFSGraph) -> List[str]:
    g.dfs()

    event_lst = [(v.id, v.finish) for v in g]
    event_lst.sort(key=lambda x: x[1], reverse=True)
    return [event[0] for event in event_lst]


if __name__ == '__main__':
    g_ = build_graph()
    event_lst_ = topological_sort(g_)
    print("--> ".join(event_lst_))

# heat griddle--> 1 Tbl Oil--> 1 egg--> 3/4 cup milk-->
# 1 cup mix--> heat syrup--> pour 1/4 cup--> turn when bubbly--> eat
