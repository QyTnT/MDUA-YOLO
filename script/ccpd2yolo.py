import shutil
import os
from shutil import copy2
import random
trainfiles = os.listdir("/Users/lxw/CCPD2020/ccpd_green/val/")
                  #（图片文件夹）
num_train = len(trainfiles)
print( "num_train: " + str(num_train) )
index_list = list(range(num_train))
print(index_list)
random.shuffle(index_list)
num = 0
trainDir = "/Users/lxw/CCPD2020/images/train/"
         #（将图片文件夹中的6份放在这个文件夹下）
validDir = "/Users/lxw/CCPD2020/images/val/"
         #（将图片文件夹中的2份放在这个文件夹下）
detectDir = "/home/li/~Pycode/yolov5-source/data/test_datasets/images/"
         #（将图片文件夹中的2份放在这个文件夹下）
for i in index_list:
    fileName = os.path.join("/Users/lxw/CCPD2020/ccpd_green/val/", trainfiles[i])
    if num < num_train*0.8:
        print(str(fileName))
        copy2(fileName, trainDir)
    # elif num < num_train*0.8:
    #     print(str(fileName))
    #     copy2(fileName, detectDir)
    else:
        copy2(fileName, validDir)
    num += 1