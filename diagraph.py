# coding: utf8


class Diagraph(object):

	def __init__(self):
		pass


vStatus = {
	'UNDISCOVERED': 1,
	'DISCOVERED': 2,
	'VISIT': 3,
}


class Vertex(object):

	def __init__(self, data):
		# 顶点所包含的数据
		self.data = data
		# 顶点的出度
		self.outDegree = 0
		# 顶点的入度
		self.inDegree = 0
		# 在遍历树种，该顶点的父顶点是谁
		self.parent = None
		# 优先级算法使用
		self.priority = 0
		self.status = vStatus.get('UNDISCOVERED')
		# 顶点被发现的时刻
		self.discovered_Time = -1
		# 顶点被访问之后的时刻
		self.finished_Time = -1


ESTATUS = {
	"UNDETERMINED": 1,
	"TREE": 2,
	"CROSS": 3,
	"FORWARD": 4,
	"BACKWARD": 5,
}


class Edge(object):

	def __init__(self, data, weight):
		# 数据
		self.data = data
		# 权重
		self.weight = weight
		self.status = ESTATUS.get('UNDETERMINED')


class GraphMatrix(object):

	def __init__(self):
		# 更好的方式是封装成矩阵，或者其他对象而不是直接暴露数组。
		# 顶点集合
		self.vertex = []
		# 边集合
		self.E = []
		self.size = len(self.vertex)
		# 边数量
		self.e_number = 0

	def nextBar(self, i, j):
		# 返回于i邻接的元素中，j之后的下一个元素
		while j >= 0:
			j -= 1
			# 判断是否存在邻接关系
			if j == -1:
				return j
			if self.exist(i, j):
				return j

	def firstNbr(self, i):
		return self.nextBar(i, self.size)

	def exist(self, i, j):

		return True if self.E[i][j] else False

	def edge(self, i, j):
		if self.exist(i, j):
			return self.E[i][j].data

	def status(self, i, j):
		if self.exist(i, j):
			return self.E[i][j].status

	def weight(self, i, j):
		if self.exist(i, j):
			return self.E[i][j].weight

	def insertEdge(self, i, j, data, weight):
		if self.exist(i, j):
			return
		# 创建一个新的边
		edge = Edge(data=data, weight=weight)
		self.E[i][j] = edge
		# 图的总体边数要+1
		self.e_number += 1
		# i的出度增加
		self.vertex[i].outDegree += 1
		# i的入度增加
		self.vertex[j].inDegree += 1


