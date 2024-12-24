import os, shutil
from sklearn.model_selection import train_test_split

val_size = 0.1
test_size = 0.1
postfix = 'jpg'
imgpath = '/Users/lxw/Augmentation/images'
txtpath = '/Users/lxw/Augmentation/txt'

os.makedirs('/Users/lxw/PCB_aug/images/train', exist_ok=True)
os.makedirs('/Users/lxw/PCB_aug//images/val', exist_ok=True)
os.makedirs('/Users/lxw/PCB_aug/images/test', exist_ok=True)
os.makedirs('/Users/lxw/PCB_aug/labels/train', exist_ok=True)
os.makedirs('/Users/lxw/PCB_aug/labels/val', exist_ok=True)
os.makedirs('/Users/lxw/PCB_aug/labels/test', exist_ok=True)

listdir = [i for i in os.listdir(txtpath) if 'txt' in i]
train, test = train_test_split(listdir, test_size=test_size, shuffle=True, random_state=0)
train, val = train_test_split(train, test_size=val_size, shuffle=True, random_state=0)

for i in train:
    print(i)
    shutil.copy('{}/{}.{}'.format(imgpath, i[:-4], postfix), '/Users/lxw/PCB_aug/images/train/{}.{}'.format(i[:-4], postfix))
    shutil.copy('{}/{}'.format(txtpath, i), '/Users/lxw/PCB_aug/labels/train/{}'.format(i))

for i in val:
    shutil.copy('{}/{}.{}'.format(imgpath, i[:-4], postfix), '/Users/lxw/PCB_aug/images/val/{}.{}'.format(i[:-4], postfix))
    shutil.copy('{}/{}'.format(txtpath, i), '/Users/lxw/PCB_aug/labels/val/{}'.format(i))

for i in test:
    shutil.copy('{}/{}.{}'.format(imgpath, i[:-4], postfix), '/Users/lxw/PCB_aug/images/test/{}.{}'.format(i[:-4], postfix))
    shutil.copy('{}/{}'.format(txtpath, i), '/Users/lxw/PCB_aug/labels/test/{}'.format(i))
