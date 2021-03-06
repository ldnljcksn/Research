from Node import Node


class Edge:
	def __init__(self, n1: Node, n2: Node, w: int):
		"""Initialize the edge with the two nodes and the weight"""
		self.node1 = n1
		self.node2 = n2
		self.weight = w

	def get_weight(self):
		return self.weight

	def get_nodes(self):
		return self.node1, self.node2
