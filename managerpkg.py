# 制 作 人：祝金宝
# 制作时间：2022/5/21 17:55
# 制作用途：仅学习（不负任何责任）

import os

def v4():
    # deb http://archive.kylinos.cn/kylin/KYLIN-ALL 4.0.2-desktop main restricted universe multiverse
    url = ['http://archive.kylinos.cn/kylin/KYLIN-ALL', '4.0.2-desktop', 'main', 'restricted','universe' , 'multiverse']
    a = url[0] + '/dists/' + url[1] + '/' +  url[2]
    b = url[0] + '/dists/' + url[1] + '/' +  url[3]
    c = url[0] + '/dists/' + url[1] + '/' +  url[4]
    d = url[0] + '/dists/' + url[1] + '/' +  url[5]
    return a, b, c, d, url


def v4sp1():
    # deb http://archive.kylinos.cn/kylin/KYLIN-ALL 4.0.2sp1-desktop main restricted universe multiverse
    url = ['http://archive.kylinos.cn/kylin/KYLIN-ALL', '4.0.2sp1-desktop', 'main', 'restricted','universe' , 'multiverse']
    a = url[0] + '/dists/' + url[1] + '/' +  url[2]
    b = url[0] + '/dists/' + url[1] + '/' +  url[3]
    c = url[0] + '/dists/' + url[1] + '/' +  url[4]
    d = url[0] + '/dists/' + url[1] + '/' +  url[5]
    return a, b, c, d, url



