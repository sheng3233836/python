#!/usr/bin/env python3
# coding=utf-8

import numpy as np

# a = np.matrix('1 2;3 4')
# b = np.array([[1], [2]])
# print(b)
# print(a * b)
# c = np.arange(9).reshape(3, 3)
# b = [[1], [2], [3]]
# print(c)
# print(c * b)  # 数组乘以数组
# c = np.matrix(c)
# print(c * b)  # 矩阵乘以数组

# np.dot 和 * 两个矩阵乘可以用*,np.dot可以用于array的矩阵乘

# shape & reshape
a = np.array([[1, 2, 3], [4, 5, 6]])
# print(a.shape)
print(a.reshape((3, 2), 1, 28, 28))

# matrix
# a = np.mat(np.arange(1, 5).reshape(2, 2))
# b = np.mat(np.arange(5, 9).reshape(2, 2))
# print(a)
# # (a) .T －－ 返回自身的转置
# # (b) .H －－ 返回自身的共轭转置
# # (c) .I －－ 返回自身的逆矩阵
# # (d) .A －－ 返回自身数据的2维数组的一个视图
# print(a.T)
# print(a.H)
# print(a.I)
# print(a.A.shape)
# print(type(a))
# print(type(a.A))

# print(np.power(a, 2))
# print(np.log(a))
# print(2 ** 2)
# print(a * 2)
# print(a / 2)

# b = np.mat(np.arange(3).reshape(1, 3))
# print(b)
# print(a + b)
# print(a * b.T)

# a = np.mat([[1], [2], [3]])
# b = np.mat([[1], [2], [3]])
# b = np.c_[b, b]
# # 使用np.c_[]和np.r_[]分别添加行和列
# print(np.c_[a, b])
#
# print(a - b)
