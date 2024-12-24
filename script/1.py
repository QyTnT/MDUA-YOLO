import shutil
import cv2
import os


def txt_file(img_path):
    x = img_path.split("/", 9)
    if x[5] == "train":
        y = '/'.join(x[0:4]) + '/labels/' + 'train/'
    else:
        y = '/'.join(x[0:4]) + '/labels/' + 'val/'
    return y


def txt_translate(path, txt_path):
    for filename in os.listdir(path):
        print(filename)

        list1 = filename.split("-", 3)  # 第一次分割，以减号'-'做分割
        subname = list1[2]
        list2 = filename.split(".", 1)
        subname1 = list2[1]
        if subname1 == 'txt':
            continue
        lt, rb = subname.split("_", 1)  # 第二次分割，以下划线'_'做分割
        lx, ly = lt.split("&", 1)
        rx, ry = rb.split("&", 1)
        width = int(rx) - int(lx)
        height = int(ry) - int(ly)  # bounding box的宽和高
        cx = float(lx) + width / 2
        cy = float(ly) + height / 2  # bounding box中心点

        img = cv2.imread(path + filename)
        if img is None:  # 自动删除失效图片（下载过程有的图片会存在无法读取的情况）
            os.remove(os.path.join(path, filename))
            continue
        width = width / img.shape[1]
        height = height / img.shape[0]
        cx = cx / img.shape[1]
        cy = cy / img.shape[0]

        txtname = filename.split(".", 1)
        txtfile = txt_path + txtname[0] + ".txt"
        # 绿牌是第0类，蓝牌是第1类
        with open(txtfile, "w") as f:
            f.write(str(0) + " " + str(cx) + " " + str(cy) + " " + str(width) + " " + str(height))


if __name__ == '__main__':
    # 修改此处地址
    trainDir = "/Users/lxw/CCPD2020/images/train/"
    validDir = "/Users/lxw/CCPD2020/images/val/"
    # 该处修改为图片存储地址
    txt_path1 = txt_file(trainDir)
    txt_path2 = txt_file(validDir)
    txt_translate(trainDir, txt_path1)
    txt_translate(validDir, txt_path2)