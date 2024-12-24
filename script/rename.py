import os

def rename_images(folder_path):
    # 遍历文件夹中的所有文件
    for filename in os.listdir(folder_path):
        if filename.endswith('.jpg') or filename.endswith('.jpeg'):
            # 拼接原文件路径
            src = os.path.join(folder_path, filename)
            # 拼接目标文件路径，去掉后缀"_test"
            dst = os.path.join(folder_path, filename.replace('_test', ''))
            # 重命名文件
            os.rename(src, dst)
            print(f'Renamed {src} to {dst}')

# 调用函数并传入文件夹路径
folder_path = '/Users/lxw/DeepPCB/pcbdata/jpg'
rename_images(folder_path)