# coding:utf8

import binary_search_tree


class AVL(binary_search_tree.BinarySearchTree):
	"""
	二叉搜索树中的平衡二叉树的一种实现AVL树，
	AVL树中引入了一个平衡因子的概念，对于一个节点它是否平衡的衡量标准是左子树的高度-右子树的高度 >=-1 <=1.否则节点就是不平衡的，
	而这个差值就是平衡因子
	"""

	def __init__(self, root):
		super(AVL, self).__init__(root)

	def balance_fac(self, node):
		# node节点的平衡因子是多少
		l_height = node.lChild.height if node.lChild else -1
		r_height = node.rChild.height if node.rChild else -1
		return l_height - r_height

	def avl_balanced(self, node):
		# node节点是否平衡
		return -1 <= self.balance_fac(node) <= 1

	def insert(self, node):
		# 调用父亲方法插入到树中
		super(AVL, self).insert(node)
		# 检查失衡的节点
		while node.parent:
			# 不平衡
			if not self.avl_balanced(node.parent):

				# 进行重新平衡reset_balance（调整平衡内会有调整高度算法）
				pass
				break
			else:
				# 只需要更新一下高度
				self.update_height(node)
			node = node.parent

	def remove(self, node):
		"""
		删除操作,删除操作最多可引起logn次的重新平衡调整
		"""
		# 调用父亲的删除操作方法,返回的是替换元素
		succ = super(AVL, self).remove(node)
		# 从self._hot开始向reset_balance
		_hot = self._hot
		while _hot:
			if not self.avl_balanced(_hot):
				# 如果不平衡,调整
				pass
				# 并且更新高度
				self.update_height(_hot)
				_hot = self._hot.parent

	def retate_at(self, a, b, c, t0, t1, t2, t3):
		"""
		3 + 4 重构法,也就是平衡调整算法，也就是说对于g, p, v这样的不平衡节点，我们重新命名为a,b,c(当然对于单旋或者双旋a,b，c是需要区分的)
		他们的中序遍历要满足abct0t1t2t3,并且b是a,c的父亲，t0t1是a的儿子，t2t3是b的儿子。
		:param a: 
		:param b: 
		:param c: 
		:param t0: 
		:param t1: 
		:param t2: 
		:param t3: 
		:return: 
		"""
		pass
