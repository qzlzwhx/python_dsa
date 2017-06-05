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
		self.key = []
		self.children = []
		self.parent = None

	def search(self, entry):
		if entry in self.key:
			return True
		else:
			return False

	def find(self, entry):
		# 那么就返回v中不大于entry的最后一个索引位置
		for index, item in enumerate(self.key):
			if item > entry:
				return index - 1

	def insert(self):
		# 这里应该使用向量，插入到index的时候，原来的index以后的数据应该向后挪动
		pass


class BinTree(object):

	def __init__(self, root):
		self.root = root
		self._hot = None
		self.size = 0
		pass

	def search(self, entry):
		# 搜索的是entry而不是node
		v = self.root

		# 搜索不到，那么就返回v中不大于entry的最后一个索引位置
		while v:
			if v.search(entry) or v is None:
				return v
			index = v.find(entry)
			child = v.children[index+1]
			self._hot = v
			v = child

	def insert(self, entry):
		# 判断entry是否在树中
		if self.search(entry):
			return False

		# 如果不存在，那么self._hot肯定就是它应该插入的叶子节点
		# 判断entry应该插入的位置，
		index = self._hot.find(entry)

		self._hot.insert(index + 1, entry)
		# 判断是否导致上溢而需要分裂
		self.solve_upper(self._hot)
		pass

	def remove(self, entry):
		pass

	def solve_upper(self, node):
		pass

	def solve_down(self, node):
		pass
