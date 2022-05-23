# 制 作 人：祝金宝
# 制作时间：2022/5/21 17:55
# 制作用途：仅学习（不负任何责任）
import re


def openfile():
    # 启发来自：https://blog.csdn.net/gao_summer_cola/article/details/85767491
    # 作者 https://github.com/hansliu-spark 参与本段代码整理
    file_object = open('Packages', 'r', encoding='UTF-8')
    package = []
    for line in file_object.readlines():
        p = re.search("^Package*", line)
        f = re.search("^Filename*", line)
        d = re.search("^Depends*", line)
        if p or f or d:
            package.append(line)
    return package


def search_pkg(job):
    # search_pkg用法：这个函数有两个返回值，他们是一串字符串    Package: fglrx\n', 'Depends
    try:
        a = openfile()
        job = 'Package: ' + job + "\n"
        b = a.index(job)
        if not a[b + 1].startswith('Depends'):
            depends = 'Depends: None'
            filename = a[b + 1].lstrip('Filename: ')
        else:
            depends = a[b + 1]
            filename = a[b + 2].lstrip('Filename: ')
    except:
        print('软件不存在')
    return depends, filename




