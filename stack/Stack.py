# coding:utf8


class Stack(object):

	def __init__(self):
		self.data = []

	def top(self):
		return self.data[-1] if len(self.data) > 0 else None

	def pop(self):
		return self.data.pop(self.size-1)

	def push(self, value):
		self.data.append(value)

	@property
	def size(self):
		return len(self.data)

	def empty(self):
		return True if len(self.data) == 0 else False
