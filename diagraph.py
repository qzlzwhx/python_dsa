# coding: utf8

import datetime

from queue import Queue


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
		self.clock = 1


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
			return self.E[i][j]

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

	def insertVerTex(self, vertex):
		self.vertex.append(vertex)
		self.size += 1
		# 增加一行
		self.E.append([0 for i in range(self.size)])
		# 每一行加一列
		for j in self.E:
			print j
			j.append(0)
		print self.E

	def breadth_first_search(self, v):
		# 广度优先遍历，思路就是从开始顶点位置出发遍历所有的邻接顶点，依次类推，知道所有所以相关邻接节点被访问
		# 注意的是，
		clock = 1
		queue = Queue()
		# 入队
		queue.enqueue(v)
		# 时钟记录
		clock += 1

		while not queue.empty():
			v = queue.dequeue()
			self.vertex[v].clock = clock
			# 循环所有的邻接元素，并分别标记
			# v的第一个邻接节点
			u = self.firstNbr(v)
			# first_nbr = self.vertex[firstNbr_index]
			while u > 0:

				vertex = self.vertex[u]
				# 如果顶点是undiscovered即未发现，那么入队，并标记为discovered，将边标记为tree，该顶点的父亲是v，并且标记时钟
				if vertex.status == vStatus.get('UNDISCOVERED'):
					# 如果顶点是undiscovered即未发现，那么入队，并标记为discovered，将边标记为tree，该顶点的父亲是v，并且标记时钟
					queue.enqueue(u)
					vertex.status = vStatus.get('DISCOVERED')
					vertex.parent = self.vertex[v]
					self.E[v][u].status = ESTATUS.get('TREE')
					clock += 1
					vertex.clock = clock
					# 记录discover_time ,
					vertex.dtime = datetime.datetime.now()
				else:
					# 否则（已入队，或者出队）标记边为cross，意思是该边跨边并不作为树
					self.E[v][u].status = ESTATUS.get('CROSS')
				u -= 1
				u = self.nextBar(v, u)
			# 标记v被访问过即visited
			self.vertex[v].status = vStatus.get('VISIT')
			print self.vertex[v].data

	# 对于多个连通域的情况
	def bfs(self, v):
		# 并不是所有的图都可以从任意一个顶点出发可以遍历所有的遍历的。比如多连通域的问题解决办法就是循环每一个顶点，进行上边代码得操作
		# 如果这个顶点是undiscovered

		# 广度优先搜索算法的事件复杂度并不是从代码上看到的n^2而是最多O(n + e) n是顶点规模，e是边数。所以这样一个算法的时间复杂度已经是极好了。
		for v in self.vertex:
			if v.status == vStatus.get('UNDISCOVERED'):
				self.breadth_first_search(v)

	def deep_first_search(self, v):
		# 深度优先搜索
		# 策略：深度优先搜索，从某个顶点V出发，从他所有的邻接节点中随机取一个如果是未访问就继续递归采用DFS搜索访问，直到所有的邻接节点
		# 被发现或者访问完，就访问节点v。具体在递归过程中对邻接节点的处理是属于算法的细节。
		# 这里引入的backward边，forward边，和cross边的意思是，backward表示从A->B的边B这个顶点已经提前被发现了。
		# forward，刚好符合树的子节点的引用比如A->B的边，这个方向上B在tree中是A的子节点。
		# cross表示2个顶点不存在父子继承关系，在图转化成树的过程中他们在树中无任何继承关系。是
		for i in range(self.size):
			if self.E[v][i]:
				# 表示v和i有一个边
				u = self.vertex[i]
				# 对u的状态进行判断
				if u.status == vStatus.get('UNDISCOVERED'):
					self.deep_first_search(i)
					# 标记支撑树的边
					self.E[v][i].status = ESTATUS.get("TREE")
					# 标记父子关系
					self.vertex[i].parent = self.vertex[v]
				elif u.status == vStatus.get('DISCOVERED'):
					# 已经被发现但是未访问应该属于被后代指向的祖先,即向后边
					self.E[v][i].status = ESTATUS.get("BACKWARD")

				else:
					# 已经访问完毕，则视为前向边或跨边,
					self.E[v][i].status = ESTATUS.get("FORWARD") if self.vertex[v].dTime < self.vertex[i].dTime \
						else ESTATUS.get('CROSS')
		# 所有的邻接节点访问完后，标记v为visited
		self.vertex[v].status = vStatus.get('VISITED')



class UnDiagraph(Diagraph):
	# 无向图

	def insertEdge(self, i, j, data, weight):
		if self.exist(i, j) or self.exist(j, i):
			return
		# 创建一个新的边
		edge = Edge(data=data, weight=weight)
		self.E[i][j] = edge
		self.E[j][i] = edge
		# 图的总体边数要+1(用有向图表示无向图所以+2)
		self.e_number += 2
		# i, j的出度增加
		self.vertex[i].outDegree += 1
		self.vertex[j].outDegree += 1
		# i, j的入度增加
		self.vertex[j].inDegree += 1
		self.vertex[i].inDegree += 1
