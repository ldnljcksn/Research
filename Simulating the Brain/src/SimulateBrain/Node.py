# import numpy as np
from typing import Dict


class Node:
	def __init__(self, n: str, v: int):
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
		if n not in self.neighbor_to_weight:
			self.neighbor_to_weight[n] = w
