# 制 作 人：祝金宝
# 制作时间：2022/5/21 20:49
# 制作用途：仅学习（不负任何责任）
import managerpkg
from requests import get


def choice():
    # 找到对应packages文件位置，下一步搜索安装包
    s = int(input("""初始化需要下载软件的系统版本
    v4  = 1           v4sp1=2
    v4sp2=4           v4sp3=4
    v4sp4=5           v10  =6
    v10sp1            packages: """))
    if s == 1:
        a = managerpkg.v4()
    elif s == 2:
        a = managerpkg.v4sp1()
    elif s == 3:
        pass
    elif s == 4:
        pass
    elif s == 5:
        pass
    elif s == 6:
        pass
    else:
        pass
    return a

def arch(url):
    x86 = 'binary-amd64/'
    arm = 'binary-arm64/'
    mips = 'binary-mips64el/'
    s = int(input('请输入架构1=x86,2=arm,3=mips：'))
    if s == 2:
        urline = url[1] + '/' + arm + 'Packages'
        a = 'x86'
    elif s > 2:
        urline = url[1] + '/' + mips + 'Packages'
        a = 'arm'
    else:
        urline = url[1] + '/' + x86 + 'Packages'
        a = 'mips'
    return urline, a


def download():
    pkg_url = arch(choice())[0]
    r = get(pkg_url)
    with open('Packages', 'wb') as f:
        f.write(r.content)



# def mkdir():
#     os.path.exists()






