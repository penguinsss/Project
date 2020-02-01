"""
文件常见操作都包含在模块中
    2个文件：
        rename  重命名文件
        remove  删除文件
    5个文件夹：
        mkdir    创建文件夹
        getcwd   获取当前路径
        chdir    切换当前路径
        listdir  列出前路径中的内容
        rmdir    删除
"""

import os

# 1、重命名文件   rename
os.rename('C:/Users/32022/Desktop/2.png', 'C:/Users/32022/Desktop/22.png')
# 2、删除文件    remove
os.remove('11.txt')
# 3、创建文件夹   mkdir
os.mkdir('demo')
# 4、获取当前路径  getcwd
print(os.getcwd())
# 5、切换当前路径  chdir
os.chdir('demo')
print(os.getcwd())
os.mkdir('demo1')
# 6、列出当前路径中的内容listdir  相当于ls，可指定文件夹
data = os.listdir()
print(data)
# 7、删除空文件夹rmdir
os.rmdir('demo')












