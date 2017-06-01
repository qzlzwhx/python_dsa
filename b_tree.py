# coding:utf8


class Entry(object):

	def __init__(self, data):
		self.data = data

	def __eq__(self, other):
		if self.data == other.data:
			return True
		else:
			return False


class BinNode(object):

	def __init__(self):
		self.entry = []
		self.children = []
		self.parent = None


class BinTree(object):

	def __init__(self, root):
		self.root = root
		pass

	def search(self, entry):
		# 搜索的是entry而不是node
		pass

	def insert(self, entry):
		pass

	def remove(self, entry):
		pass

	def solve_upper(self, entry):
		pass

	def solve_down(self, entry):
		pass
