# 制 作 人：祝金宝
# 制作时间：2022/5/21 17:55
# 制作用途：仅学习（不负任何责任）

import search_url, requests, re
from seach_package import *


def main():
    # search_url.download()
    s = input('请输入需要搜索的软件:')
    depend, filename = search_pkg(s)
    url = filename.split('\n')
    url = 'http://archive.kylinos.cn/kylin/KYLIN-ALL/' + url[0]
    file = filename.split('/')[-1].rsplit("\n")
    file = file[0]
    # kv = {'User-agent': 'Mozilla/5.0'}  # headers=kv
    deb = requests.get(url)
    # print(deb.status_code)
    with open(file, 'wb') as f:
        f.write(deb.content)
        f.close()
    line = int(input('是否下载依赖1=download：'))
    if line == 1:
        c = re.split('Depends:|\\(.*?\\)|,|\n', depend)
        # re.split('Depends:|\\(.*?\\)|,|\n', s)
        c = [x.strip() for x in c if x.strip() != '']
        print(c)
        for i in c:
            try:
                print(i)
                url1 = search_pkg(i)[1].split(',')
                url1 = 'http://archive.kylinos.cn/kylin/KYLIN-ALL/' + url1[0]
                print(url1.rsplit('\n'))
                url1 = url1.rsplit('\n')[0]
                dependfile = (url1.split('/'))[-1]
                # kv = {'User-agent': 'Mozilla/5.0'}  # headers=kv
                deb1 = requests.get(url1)
                # print(deb.status_code)
                with open(dependfile, 'wb') as f:
                    f.write(deb1.content)
                    f.close()

            except:
                print(i + '软件包不在此文件中，请增加其他Package文件')
                continue


    return print('重新发布请遵守GPLv2协议')


while True:
    try:
        main()
    except:
        print('软件不存在，是否增加源文件？Yes/No')
        break






