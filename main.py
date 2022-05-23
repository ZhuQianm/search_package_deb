# 制 作 人：祝金宝
# 制作时间：2022/5/21 17:55
# 制作用途：仅学习（不负任何责任）

import search_url, requests
from seach_package import *


def main():
    # search_url.download()
    s = input('请输入需要搜索的软件:')
    url = search_pkg(s)[1].split('\n')
    print(url[0])
    url = 'http://archive.kylinos.cn/kylin/KYLIN-ALL/' + url[0]
    file = search_pkg(s)[1].split('/')[-1].rsplit("\n")
    file = file[0]
    # kv = {'User-agent': 'Mozilla/5.0'}  # headers=kv
    deb = requests.get(url)
    # print(deb.status_code)
    with open(file, 'wb') as f:
        f.write(deb.content)
        f.close()
    return print('重新发布请遵守GPLv2协议')


while True:
    main()






