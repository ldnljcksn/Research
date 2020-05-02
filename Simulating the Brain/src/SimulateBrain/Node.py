import numpy as np


class Node:
	def __init__(self, n):
		self.name = n
		self.value = np.random.randint(0, 2)
		self.connected_to = list()

	def print_value(self):
		print("Node's value is " + str(self.value))
		return None

	def set_value(self, v):
		self.value = v
		return None

	def add_connection(self, n):
		if n not in self.connected_to:
			self.connected_to.append(n)
			self.connected_to.sort()
