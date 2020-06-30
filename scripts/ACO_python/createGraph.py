#!/usr/bin/env python
#coding=utf-8
# 輸入點 並且 計算 各自的距離
import numpy as np
import matplotlib
import matplotlib.pyplot as plt # 為了繪製出圖形
# 4 nodes
# x=[0.09,0.16,0.84,0.70 ] # 以list的形式
# y=[0.17,0.52,0.92,0.16]

# 原點+9 個節點 原點設為index 0
x = [0,19.47000,-6.47000,40.09000,5.39000,15.23000,-10,-20.47000,5.20000,16.30000]
y = [0,6.10000,-4.44000,-1.54000,6.37000,7.24000,4.05000,7.02000,7.666,-7.38000]

# 14 個節點
# x = [16.47000,16.47000,20.09000,22.39000,25.23000,22,20.47000,17.20000,16.30000,14.05000,16.53000,21.52000,19.41000,20.09000]
# y = [96.10000,94.44000,92.54000,93.37000,97.24000,96.05000,97.02000,96.29000,97.38000,98.12000,97.38000,95.59000,97.13000,94.55000]

# 繪製圖型 ============================================================================================================================

# plt.scatter(x,y)
plt.show()




# ====================================================================================================================================
n=len(x) # 知道總共有幾個點

node=np.zeros((n,2)) # node 是2維矩陣
for i in range(n):
    node[i,0]=node[i,0]+x[i]
    node[i,1]=node[i,1]+y[i]
    # print('點的座標: \n', node)

edge=np.zeros((n,n)) # 創造點跟點的距離矩陣
for i in range(n):
    for j in range(n):
        x1=node[i,0]
        x2=node[j,0]
        y1=node[i,1]
        y2=node[j,1]
        edge[i,j]=((x1-x2)**2+(y1-y2)**2)**0.5
# for i in range(n):
#     edge[i,i]=0.0000000000000000001 # 不能除以0 所以換成極小值

def nodenum():
    return n

def nodes():
    return node

def edges():
    return edge
