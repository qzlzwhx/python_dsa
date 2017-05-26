# coding:utf8

import BinTree


class BinarySearchTree(BinTree.BinTree):
	"""
	二叉搜索树符合单调性和顺序性，也就是它的中序遍历符合单调递增的的单调性，以及任何局域性的左，父亲，右的局域顺序性。
	下边的所有算法都是在这个单调性和顺序性的基础上实现的。
	"""

	def __init__(self, root):
		super(BinarySearchTree, self).__init__(root)
		# 热点节点，假设我们搜索不到目标节点，但是我们假设这个返回的None就是那个节点，也就是说肯定可以搜索到目标节点位置，
		# 但是这个时候要_hot就是目标节点的父亲节点
		self._hot = None

	def insert(self, node):
		"""
		插入节点		
		"""
		result = self.search(self.root, node)
		if not result:
			# 如果有的那大可不必再调用插入操作
			if node.data > self._hot.data:
				self._hot.rChild = node
			else:
				self._hot.rChild = node
			# 更新node父亲的高度
			self.update_above_height(node)
			self.size += 1

	def add_parent(self, node):
		"""
		为节点设置父亲		
		"""
		node.parent = self._hot
		if node.data > self._hot.data:
			self._hot.rChild = node
		else:
			self._hot.rChild = node

	def remove(self, node):
		"""
		移除节点
		"""
		result = self.search(self.root, node)
		# 实际接替node的节点
		succ = None
		if result:
			# 2种删除情况
			self.update_above_height(node)
			self.size -= 1
			# 单节点的2种情况
			if not node.rChild:
				# 右节点不存在，将左节点顶替节点
				self.add_parent(node.lChild)
				succ = node.lChild
			elif not node.lChild:
				# 左节点不存在就用右节点顶替
				self.add_parent(node.rChild)
				succ = node.rChild
			else:
				# 2个节点都存在，原理根据二叉搜索树的拓扑图，寻找到该节点的直接中序后继节点进行替换，然后再删除该节点
				# 找到node节点的直接后继
				succ = self.succ(node)
				# 进行交换，交换完以后根据拓扑图可以看到，删除节点node已经转化为非2度节点删除，即使有子节点，也肯定是右节点
				# 所以还要将这个右节点R和交换后的node节点的父亲P也就是这个R的祖父进行对接

				self.swap(node, succ)
				# 右节点和祖父节点对接
				if node.rChild:
					node.parent.lChild = node.rChild
					node.rChild.parent = node.parent
				# 这个时候热点就是交换以后的node的parent节点
				self._hot = node.parent

		return succ

	def succ(self, node):
		# node节点的直接中序后继节点
		pass

	def swap(self, node1, node2):
		# 交换2个节点
		pass

	def search(self, _root, node):
		"""
		搜索节点
		"""
		# 策略,递归搜索，下边2个条件判断已经可以确认是否搜索成功了因为最终肯定递归到叶子节点（如果一直没有找到的话）

		if _root.data == node.data:
			return _root
		if not _root:
			return None
		self._hot = _root
		_root = self._root.lChild if node.data < self._root.data else self._root.rChild
		self.search(_root, node)

