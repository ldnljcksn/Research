from typing import Dict


class Node:
	def __init__(self, n: str, v: int):
		"""Initialize the Node with a given name and value"""
		self.name = n
		self.value = v
		self.neighbor_to_weight: Dict[Node, int] = {}

	def print_value(self):
		print("Node's value is " + str(self.value))
		return None

	def set_value(self, v: int):
		self.value = v
		return None

	def add_connection(self, n, w: int):
		"""Add a node as a neighbor and give the weight of the edge"""
		if n not in self.neighbor_to_weight:
			self.neighbor_to_weight[n] = w
