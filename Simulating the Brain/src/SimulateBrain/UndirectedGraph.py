from Node import Node
from Edge import Edge
from typing import List


class UndirectedGraph:
	nodes: List[Node] = []
	edges: List[Edge] = []

	def add_node(self, node: Node):
		if node not in self.nodes:
			self.nodes.append(node)

	def add_edge(self, edge: Edge):
		if edge not in self.edges:
			self.edges.append(edge)
			edge.node1.add_connection(edge.node2, edge.weight)
			edge.node2.add_connection(edge.node1, edge.weight)

	def print_graph(self):
		for i in self.nodes:
			print(i.name + '(' + str(i.value) + '): ', end='')
			for j in i.neighbor_to_weight.keys():
				print(j.name + '(' + str(j.neighbor_to_weight.get(i)) + ') ', end='')
			print()

		print('Done')

	def iterate_graph(self):
		for i in self.nodes:
			for j in i.neighbor_to_weight.keys():
				if i.value == 0:
					if i.neighbor_to_weight.get(j) == 1 and j.value == 1:
						i.set_value(1)
				if i.value == 1:
					if i.neighbor_to_weight.get(j) == -1 and j.value == 0:
						i.set_value(0)
