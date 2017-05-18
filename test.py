# coding:utf8

from stack.Stack import Stack
from BinTree import BinNode, BinTree


root = BinNode('R')

A = BinNode("A")
B = BinNode("B")
C = BinNode("C")
D = BinNode("D")
E = BinNode("E")
F = BinNode("F")
G = BinNode("G")
H = BinNode("H")
J = BinNode("J")

tree = BinTree(root)

tree.insertASLC(root, A)
tree.insertAsRC(root, B)
tree.insertASLC(A, C)
tree.insertAsRC(A, D)
tree.insertASLC(B, E)
tree.insertAsRC(B, F)
tree.insertASLC(C, G)
tree.insertAsRC(F, H)
tree.insertAsRC(D, J)

# def traversal1(parent):
# 	# 递归遍历先序遍历即：parent, lchild, rchild的顺序
# 	if not parent:
# 		return
# 	print parent.data
# 	traversal1(parent.lChild)
# 	traversal1(parent.rChild)

print 'start...................'
# tree.traversal1(root)
# tree.traversal2(root)
tree.mid_order_traversal2(root)
#
# import random
# result = []
# random.randint(100000000000000, 999999999999999)
# while len(result) < 100:
# 	num = random.randint(100000000000000, 999999999999999)
# 	if num not in result:
# 		result.append(num)
# print result
