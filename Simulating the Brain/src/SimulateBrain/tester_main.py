from Node import Node
from UndirectedGraph import UndirectedGraph


g = UndirectedGraph()
a = Node('A')
g.add_node(a)
g.add_node(Node('B'))
for i in range(ord('A'), ord('K')):
	g.add_node(Node(chr(i)))

edges = []
for i in range(ord('A'), ord('K')):
	for j in range(ord('A'), ord('K')):
		if i != j:
			edges.append(chr(i) + chr(j))

for edge in edges:
	g.add_edge(edge[:1], edge[1:])

g.print_nodes()
g.print_graph()
