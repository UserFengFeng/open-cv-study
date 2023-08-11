#!/user/bin/env python3
# -*- coding: utf-8 -*-

import cv2
import numpy as np
from cv2 import dnn

# 物体分类
# 导入模型、创建神经网络
config = "./model/bvlc_googlenet.prototxt"
model = "./model/bvlc_googlenet.caffemodel"

net = dnn.readNetFromCaffe(config, model)

# 读图转张量
img = cv2.imread("../smallcat.jpeg")
blob = dnn.blobFromImage(img,
                         1.0,  # 缩放因子
                         (224, 224),  # 尺寸大小
                         (104, 117, 123)  # 平均差值
                         )

# 将张量输入到网络中、并进行预测
net.setInput(blob)
r = net.forward()

# 显示结果
classed = []
path = "./model/synset_words.txt"
with open(path, 'rt') as f:
    classed = [x[x.find(" ") + 1:] for x in f]

order = sorted(r[0], reverse=True)
z = list(range(0, 3))
for i in range(0, 3):
    z[i] = np.where(r[0] == order[i])[0][0]
    print(f" {i} , compose: {classed[z[i]]}", end="")
    print(f"class row:{z[i] + 1}  possi:{order[i]}")
