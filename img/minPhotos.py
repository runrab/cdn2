from PIL import Image
import os

# Mpath = os.getcwd()
# print(Mpath)

# 原来文件夹
source_dirs = './max'
# 目标文件夹
target_dirs = './mid'
# 目标文件夹2
target_dirs2 = './min'


# 得到图片的链接
def getListFiles(path):
    assert os.path.isdir(path), '%s not exist.' % path
    ret = []
    # 已经有的文件夹
    has_dirs = []
    # 目录创建
    for root, dirs, files in os.walk(path):
        # print('%s, %s, %s' % (root, dirs, files))
        # print('%s, %s' % (dirs,files))
        s = ''.join(root) + '/' + ''.join(dirs)
        s = s.replace('\\', '/')
        # s = s.replace(source_dirs, target_path)
        if s not in has_dirs:
            has_dirs.append(s)
        if path == source_dirs:
            create_dirs(has_dirs)
        # print(s)
        # if not os.path.exists(s):
        #    os.makedirs(s)
        for filesPath in files:
            ret.append(os.path.join(root, filesPath))
    # print(ret)
    return ret


# 创建不存在文件夹
def create_dirs(has_dirs):
    for i in has_dirs:
        i = i.replace(source_dirs, target_dirs)
        if not os.path.exists(i):
            os.makedirs(i)
    for i in has_dirs:
        i = i.replace(source_dirs, target_dirs2)
        if not os.path.exists(i):
            os.makedirs(i)


# 缩放
def scale(i):
    img = Image.open('' + i)
    # 目标地址
    bb = i.replace(source_dirs, target_dirs2)
    bb = bb.replace('\\', '/')
    width, height = img.size
    w_s = int(width / (width/800))  # 长宽缩小两倍
    h_s = int(height / (height/400))  # 长宽缩小两倍
    img = img.resize((w_s, h_s), Image.ANTIALIAS)
    blank = (w_s - h_s) / 2
    #region = img.crop((0, -blank, w_s, w_s - blank))
    region = img.crop((0, 0, w_s, h_s))
    region.save(bb)


# 裁剪
def resize(i):
    img = Image.open('' + i)
    # 目标地址
    bb = i.replace(source_dirs, target_dirs)
    bb = bb.replace('\\', '/')
    width, height = img.size
    he = (width * 400) / 1920
    wi = (height - he) / 2
    # print(he)
    # print(width,height)
    # 前两个坐标点是左上角坐标
    # 后两个坐标点是右下角坐标
    # width在前， height在后
    box = (0, wi, width, he + wi)
    region = img.crop(box)
    # cc=bb.replace('\\','')
    # if os.path.exists(cc):
    # os.makedirs(cc)
    # 因为保存裁剪后的文件要求文件夹要存在故单独处理
    region.save(bb)


def declImg():
    a = getListFiles(source_dirs)
    b = getListFiles(target_dirs)
    c = getListFiles(target_dirs2)
    for i in a:
        if i not in b:
            b.append(i)
            resize(i)
        if i not in c:
            c.append(i)
            scale(i)


declImg()

##图片缩小


'''
#导出require.txt
#pip freeze > requirements.txt
img = Image.open('01.jpg')
width, height = img.size

# 前两个坐标点是左上角坐标
# 后两个坐标点是右下角坐标
# width在前， height在后
box = (100, 100, 550, 350)

region = img.crop(box)
region.save('crop.jpg')
'''
