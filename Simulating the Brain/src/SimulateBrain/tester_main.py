from Node import Node
from Edge import Edge
import numpy as np
from UndirectedGraph import UndirectedGraph


def rand_node_val():
	return np.random.randint(0, 2)


def rand_edge_weight():
	rand_num = np.random.randint(0, 4)
	if rand_num == 0:
		return -1
	if rand_num == 1:
		return 1
	else:
		return 0


def main():
	# g = UndirectedGraph()
	# a = Node('A')
	# g.add_node(a)
	# g.add_node(Node('B'))
	# for i in range(ord('A'), ord('K')):
	# 	g.add_node(Node(chr(i)))
	#
	# edges = []
	# for i in range(ord('A'), ord('K')):
	# 	for j in range(ord('A'), ord('K')):
	# 		if i != j:
	# 			edges.append(chr(i) + chr(j))
	#
	# for edge in edges:
	# 	g.add_edge(edge[:1], edge[1:])

	# a = Node('A', rand_node_val())
	# b = Node('B', rand_node_val())
	# c = Node('C', rand_node_val())
	#
	# ab = Edge(a, b, rand_edge_weight())
	# bc = Edge(b, c, rand_edge_weight())

	a = Node('A', 0)
	b = Node('B', 1)
	c = Node('C', 0)

	ab = Edge(a, b, -1)
	bc = Edge(b, c, -1)

	g = UndirectedGraph()
	g.add_node(a), g.add_node(b), g.add_node(c)
	g.add_edge(ab), g.add_edge(bc)

	# g.print_nodes()
	g.print_graph()

	finished = False
	while not finished:
		print('What would you like to do?')
		print('(1) iterate graph')
		print('(2) end')
		user_input = input()
		if user_input == str(1):
			g.iterate_graph()
			g.print_graph()
		if user_input == str(2):
			finished = True


main()
