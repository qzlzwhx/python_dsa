# coding:utf8


class Queue(object):

	def __init__(self):
		self.data = []

	def enqueue(self, value):
		self.data.append(value)

	def dequeue(self):
		return self.data.pop(0) if self.data else None

	def empty(self):
		return False if self.data else True

	def front(self):
		return self.data[0] if self.data else None
