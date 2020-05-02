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

	g = UndirectedGraph()

	print('Please choose an action:')
	print('(1) Build random graph of size n')
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
		g.print_num_nodes_on()
		# g.print_edges_ex_or_in()
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
			g.print_num_nodes_on()
			# g.print_edges_ex_or_in()
		if user_input == str(2):
			g.print_nodes()
		if user_input == str(3):
			g.print_graph()
		if user_input == str(0):
			finished = True


main()
