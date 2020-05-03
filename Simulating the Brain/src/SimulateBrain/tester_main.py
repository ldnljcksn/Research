from Node import Node
from Edge import Edge
from UndirectedGraph import UndirectedGraph
import numpy as np


def rand_node_val():
	"""Returns a random value 0 or 1, 50/50 chance"""
	return np.random.randint(0, 2)


def rand_edge_weight(in_prob=25, no_prob=50, ex_prob=25):
	"""Returns a random edge weight of -1 (inhibiting), 0 (no edge), or 1 (exciting)

	Precondition: in_prob + no_prob + ex_prob == 100"""
	rand_num = np.random.randint(0, in_prob + no_prob + ex_prob)
	if rand_num < in_prob:
		return -1
	elif rand_num < in_prob + no_prob:
		return 0
	else:
		return 1


def main():
	# Build the graph
	g = UndirectedGraph()

	print('Please choose an action:')
	print('(1) Build random graph of size n')
	print('(2) Use standard graph')
	print('(3) Build manual graph')
	user_input = input()

	# Build random graph of size n
	if user_input == str(1):
		graph_size = int(input('n = '))
		for i in range(0, graph_size):
			new_node = Node(str(i + 1), rand_node_val())
			g.add_node(new_node)
		for i in g.nodes:
			for j in g.nodes:
				if i.name == j.name:
					edge_weight = 0
				else:
					edge_weight = rand_edge_weight()
				new_edge = Edge(i, j, edge_weight)
				g.add_edge(new_edge)
		g.print_num_nodes_on()

	# Build pre-made graph
	if user_input == str(2):
		user_input = input('Please choose standard graph (1) exciting, (2) inhibiting, or (3) none:  ')
		if user_input == str(1):
			a = Node('A', 0)
			b = Node('B', 1)
			c = Node('C', 0)
			edge_weight = 1
		elif user_input == str(2):
			a = Node('A', 1)
			b = Node('B', 1)
			c = Node('C', 1)
			edge_weight = -1
		elif user_input == str(3):
			a = Node('A', 0)
			b = Node('B', 1)
			c = Node('C', 0)
			edge_weight = 0
		else:
			print('Response not valid, defaulted to (1) exciting')
			a = Node('A', 0)
			b = Node('B', 1)
			c = Node('C', 0)
			edge_weight = 1
		ab = Edge(a, b, edge_weight)
		bc = Edge(b, c, edge_weight)
		g.add_node(a), g.add_node(b), g.add_node(c)
		g.add_edge(ab), g.add_edge(bc)
		g.print_num_nodes_on()

	# Build manual graph
	if user_input == str(3):
		graph_size = int(input('n = '))
		nodes_on = int(input('How many nodes on?  '))
		for i in range(0, graph_size):
			if i < nodes_on:
				node_val = 1
			else:
				node_val = 0
			new_node = Node(str(i + 1), node_val)
			g.add_node(new_node)
		in_prob = int(input('Probability of inhibiting edge (in %):  '))
		no_prob = int(input('        Probability of no edge (in %):  '))
		ex_prob = int(input('  Probability of exciting edge (in %):  '))
		for i in g.nodes:
			for j in g.nodes:
				if i.name == j.name:
					edge_weight = 0
				else:
					edge_weight = rand_edge_weight(in_prob, no_prob, ex_prob)
				new_edge = Edge(i, j, edge_weight)
				g.add_edge(new_edge)
		g.print_num_nodes_on()

	finished = False
	while not finished:
		print('What would you like to do?')
		print('(1) iterate graph once')
		print('(2) print node list')
		print('(3) print full graph')
		print('(0) exit')
		user_input = input()

		# Iterate graph
		if user_input == str(1):
			g.iterate_graph()
			g.print_num_nodes_on()

		# Print list of nodes and their value
		if user_input == str(2):
			g.nodes.sort(key=lambda x: int(x.name))
			g.print_nodes()

		# Print full graph
		if user_input == str(3):
			g.print_graph()

		# Exit
		if user_input == str(0):
			finished = True


main()
