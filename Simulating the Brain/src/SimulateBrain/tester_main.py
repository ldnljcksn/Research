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
	# a = Node('A', 0)
	# b = Node('B', 1)
	# c = Node('C', 0)
	#
	# ab = Edge(a, b, -1)
	# bc = Edge(b, c, -1)
	#
	# g = UndirectedGraph()
	# g.add_node(a), g.add_node(b), g.add_node(c)
	# g.add_edge(ab), g.add_edge(bc)
	#
	# g.print_graph()

	g = UndirectedGraph()

	print('Please choose an action:')
	print('(1) Build random graph of size n')
	# print('(2) Manually build graph')
	user_input = input()
	if user_input == str(1):
		graph_size = int(input('n = '))
		for i in range(0, graph_size):
			new_node = Node(str(i + 1), rand_node_val())
			g.add_node(new_node)
		for i in g.nodes:
			for j in g.nodes:
				new_edge = Edge(i, j, rand_edge_weight())
				g.add_edge(new_edge)
	# if user_input == str(2):
	# 	finished = False
	# 	while not finished:
	# 		print('Please choose an action:')
	# 		print('(1) Add a node')
	# 		print('(2) Add an edge')
	# 		user_input = input()
	# 		if user_input == str(1):
	# 			node_name = input('Node name: ')
	# 			node_value = input('Node value: ')
	# 			new_node = Node(node_name, int(node_value))
	# 			g.add_node(new_node)
	# 		if user_input == str(2):
	# 			node1 = input('Node 1: ')
	# 			node2 = input('Node 2: ')
	# 			weight = input('Weight: ')
	# 			node1 = g.nodes.
	# 			new_edge = Edge(node1, node2, weight)
	# 			g.add_edge(new_edge)

	finished = False
	while not finished:
		print('What would you like to do?')
		print('(1) iterate graph once')
		print('(2) print node list')
		print('(3) print full graph')
		print('(0) end')
		user_input = input()
		if user_input == str(1):
			g.iterate_graph()
			print('Number of nodes on: ' + str(g.num_nodes_on()))
			print()
		if user_input == str(2):
			g.print_nodes()
		if user_input == str(3):
			g.print_graph()
		if user_input == str(0):
			finished = True


main()
