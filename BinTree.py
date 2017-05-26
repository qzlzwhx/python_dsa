# coding:utf8

from stack.Stack import Stack
from queue import Queue


class BinNode(object):

	def __init__(self, data):
		self.data = data
		self.lChild = None
		self.rChild = None
		# 单节点是0，空是-1
		self.height = 0
	#
	# def insert_as_LC(self, lChild):
	# 	self.lChild = lChild
	# 	lChild.parent = self
	#
	# def insert_as_RC(self, rChild):
	# 	self.rChild = rChild
	# 	rChild.parent = self


class BinTree(object):

	def __init__(self, root):
		self.root = root
		self.size = 0
		self.pre_order_sequnece = []

	def insertASLC(self, parent, lChild):
		parent.lChild = lChild
		lChild.parent = parent
		self.update_above_height(lChild)
		self.size += 1

	def insertAsRC(self, parent, rChild):
		parent.rChild = rChild
		rChild.parent = parent
		self.update_above_height(rChild)
		self.size += 1

	def update_height(self, node):
		lChild_height = node.lChild.height if node.lChild else -1
		rChild_height = node.rChild.height if node.rChild else -1
		node.height = 1 + max(lChild_height, rChild_height)

	def update_above_height(self, node):
		self.update_height(node)
		# 更新node上边的节点
		parent = node.parent
		while parent:
			# 优化空间如果树的高度未变化就跳出循环
			self.update_height(parent)
			parent = parent.parent

	def pre_order_traversal1(self, parent):
		# 递归遍历先序遍历即：parent, lchild, rchild的顺序
		if not parent:
			return
		print parent.data
		self.pre_order_traversal1(parent.lChild)
		self.pre_order_traversal1(parent.rChild)

	def pre_order_traversal2(self, parent):
		# 迭代版本1
		# 这里的是采用的尾递归思想，一般尾递归都可以转化成迭代
		# 思想：采用一个栈，将跟节点放入栈中，然后循环从栈中pop栈顶元素，直到栈空。如果栈顶元素有右节点就推入栈中，如果有左节点再推入左节点
		# 注意是先推入右节点
		s = Stack()
		s.push(parent)
		while not s.empty():
			node = s.pop()
			print node.data
			# 先推入有节点，因为栈是LIFO,左节点后入会先取出来访问，然后依次的递归，
			if node.rChild:
				s.push(node.rChild)
			if node.lChild:
				s.push(node.lChild)

	def pre_order_traversal3Left(self, parent, s):
		# 第三个版本的先序遍历
		# 思想：依次次访问树最左边的所有的节点，知道底部，在访问过程中如果节点有右节点，就一次放入栈中
		# 直到最后，从栈中pop出来节点继续使用本方法调用
		# s = Stack()
		# s.push()
		while parent:
			print parent.data
			s.push(parent.rChild)
			parent = parent.lChild

	def pre_order_traversal3(self, parent):
		s = Stack()
		while True:
			self.pre_order_traversal3Left(parent, s)
			if s.empty():
				break
			parent = s.pop()

	def mid_order_traversal1(self, parent):
		if not parent:
			return
		# 递归中序遍历1
		self.mid_order_traversal1(parent.lChild)
		print parent.data
		self.mid_order_traversal1(parent.rChild)

	def goAlongLeftBranch(self, parent, s):
		# 沿着根节点的所有左节点直到叶节点，将节点放入栈中
		while parent:
			s.push(parent)
			parent = parent.lChild

	def mid_order_traversal2(self, parent):
		# 迭代方式，
		s = Stack()
		while True:
			# 沿着左节点一直到叶节点（）
			self.goAlongLeftBranch(parent, s)
			if s.empty():
				break
			# 从栈顶取出一个元素继续进行上述操作，也就是最底下的叶子节点获得访问数据权
			parent = s.pop()
			print parent.data
			# 它这个时候按照中序的规则应该讲访问权交给右节点，对右节点继续重复执行上述策略
			parent = parent.rChild

	def layer_order_traversal(self, parent):
		# 层次遍历
		queue = Queue()
		if not parent:
			return
		# 将parent推入队列中
		queue.enqueue(parent)
		while True:
			# 出队列一个元素并访问
			parent = queue.dequeue()
			print parent.data
			# 将左右孩子入队（根据队列的先进先出的原则，节点逐层的被入队）
			if parent.lChild:
				queue.enqueue(parent.lChild)
			if parent.rChild:
				queue.enqueue(parent.rChild)
			if queue.empty():
				break


