from Node import Node
import numpy as np
import random


class UndirectedGraph(object):
	nodes = {}
	edges = []
	edge_indices = {}

	def add_node(self, node):
		if isinstance(node, Node) and node.name not in self.nodes:
			self.nodes[node.name] = node
			for row in self.edges:
				row.append(0)
			self.edges.append([0] * (len(self.edges) + 1))
			self.edge_indices[node.name] = len(self.edge_indices)
			return True
		else:
			return False

	def add_edge(self, node1, node2, weight=0):
		ex_or_in = random.randint(0, 3)
		if ex_or_in == 3:
			weight = 1
		if ex_or_in == 2:
			weight = -1

		if node1 in self.nodes and node2 in self.nodes:
			self.edges[self.edge_indices[node1]][self.edge_indices[node2]] = weight
			self.edges[self.edge_indices[node2]][self.edge_indices[node1]] = weight
			return True
		else:
			return False

	def print_graph(self):
		print('  ', end='')
		for i in self.edge_indices:
			print('{:>3}'.format(i + ' '), end='')
		print(' ')
		for v, i in sorted(self.edge_indices.items()):
			print(v + ' ', end='')
			for j in range(len(self.edges)):
				print('{:>3}'.format(str(self.edges[i][j]) + ' '), end='')
			print(' ')

	def print_nodes(self):
		for i in self.nodes.keys():
			print(i + ' ', end='')
		print(' ')
		for i in self.nodes.values():
			print(str(i.value) + ' ', end='')
		print('\n')

	# def iterate_graph(self):
	# 	for i in self.nodes.values():

