# 制 作 人：祝金宝
# 制作时间：2022/5/21 20:49
# 制作用途：仅学习（不负任何责任）
import re
from seach_package import *
import requests


def depend(b='fglrx-amdcccle'):
    url1 = search_pkg(b)
    depends, filename = url1
    # line = int(input('是否下载依赖1=download：'))
    line = 1
    if line == 1:
        c = re.split('Depends:|\\(.*?\\)|,|\n', depends)
        # re.split('Depends:|\\(.*?\\)|,|\n', s)
        c = [x.strip() for x in c if x.strip() != '']
        print(c)
        for item in c:
            try:
                print(item)
                url1 = search_pkg(item)[1].split(',')
                url1 = 'http://archive.kylinos.cn/kylin/KYLIN-ALL/' + url1[0]
                file1 = filename.split('/')[-1].rsplit("\n")
                file1 = file1[0]
                # kv = {'User-agent': 'Mozilla/5.0'}  # headers=kv
                deb1 = requests.get(url1)
                # print(deb.status_code)
                with open(file1, 'wb') as f:
                    f.write(deb1.content)
                    f.close()

            except:
                print(item + '不在main的Package文件中')
                continue


depend()