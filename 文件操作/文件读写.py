"""
    文件中的数据会保存到硬盘中（断电不丢失）；将数据保存到硬盘中，称为 数据持久化
"""
"""
    读写文件前，我们先必须了解一下，在磁盘上读写文件的功能都是由操作系统提供的，现代操作系统不允许普通的程序直接操作磁盘，
所以，读写文件就是请求操作系统打开一个文件对象；
    通过操作系统提供的接口  从这个文件对象  中读取数据（读文件），或者把数据写入这个文件对象（写文件）。
"""

'''
♥ r : 默认访问模式
    1> 只读模式；
    2> 文件不存在报错；   
'''
# 4种读法：如果文件很小，read()一次性读取最方便；如果不能确定文件大小，反复调用read(size)比较保险；如果是配置文件，调用readlines()最方便：
# read()：将文件中内容全部取出来
# read(size)：读取size个字节的内容
# readline() ：读取一行数据   ★主要使用这个方法, 有效的避免出现内存峰值
# readlines()：读取所有的行，每行内容作为一个元素

# read()  将文件中内容全部取出来
with open('123.txt', encoding='utf-8') as f:
    content = f.read()
    print(content)

# read(size)  读取指定大小的 字节 数量
with open('123.txt', encoding='utf-8') as f:
    content = f.read(3)
    print(content, end='')

# readline()  读取一行数据
with open('123.txt', encoding='utf-8') as f:
    content = f.readline()
    print(content, end='')  # print默认具有换行能力，可以设置end=''取消换行
    content = f.readline()
    print(content, end='')
    content = f.readline()
    print(content, end='')

# readlines() 读取所有的行，每行内容作为一个元素保存在列表中
with open('456.txt') as f:
    list_temp = f.readlines()
    for line in list_temp:
        print(line.strip())  # 把末尾的'\n'删掉
    print(list_temp)  # ['dddd\n', 'ddddddddddddd\n', 'ddddddddddddddddd\n', 'dddddddddd']

# 456.txt内容:
# dddd
# ddddddddddddd
# ddddddddddddddddd
# dddddddddd

# 一般的读取方案
with open('456.txt') as f:
    while True:
        content = f.readline()      # ★主要使用这个方法,有效的避免出现内存峰值
        print(content, end='')
        if len(content) == 0:   # 也可以是: content == ''
            break

'''
♥ w : 
    1> 只能写；
    2> 文件不存在新建；
    3> 存在会清空原内容，然后写入新内容；
    4> 同一个文件对象多次写入时追加写入，不会覆盖；
    5> 此方法写入的同时，还会返回此次写入的字符数；
'''

with open('123.txt', 'w') as f:
    n1 = f.write('cads')
    n2 = f.write('Oriya')
print(n1, n2)

'''
♥ a : 
    只能写；
    文件不存在新建；   
    存在会追加内容；
'''


'''
♥ r+ 读写模式: 
    1> 能写，打开不存在的文件会报错
    2> 存在会覆盖原内容，新写入多少字符，就会覆盖多少原文本多少字符，指针就停留在新写入内容后，此时读取会把指针后的内容读出来显示
    3> 在同一个文件对象多次写入时不会覆盖写，会追加写入；
    4> 此方法写入的同时，还会返回此次写入的字符数；
'''
# 原内容：   原内容在python解释器看来是这样的:  123456\n678\n789
# 123456
# 678
# 789

# 新内容
# 123456
# 678
# 78900
f = open('1.txt', 'r+')
f.write('000\n')
content = f.read()
print(content, end='')  # 新写入的000\n会覆盖原文件中的前5个字符，且read后显示的内容不包含新写入的内容

'''
♥ w+ :     
    1> 写读
    2> ⽂件存在则先清空内容
    3> ⽂件不存在，创建新⽂件
'''
str1 = "Hello, everyone. I'm a python programmer "
str2 = "If哈哈ffams"
with open("1.txt", "w+", encoding='utf-8') as file:
    file.write(str1)
    file.write(str2)
    file.seek(0)
    content = file.read()
    print(content)

'''
♥ a+ :      
    1> ⽤于读写
    2> ⽂件存在, 追加内容
    3> ⽂件不存在，创建新⽂件
'''
f = open('3.txt', 'a+')
f.seek(0)       # seek只对读有效
res = f.write('sssssss')
f.seek(0)
res1 = f.read()
print(res1, end='')



#     对图片、音频等非文本文件 读写 需要使用 rb wb ab
#     rb      ⼆进制格式的只读操作。后续⽹络课程中具体讲解。
#     wb      ⼆进制格式的只写操作。后续⽹络课程中具体讲解。
#     ab      ⼆进制格式的追加操作。后续⽹络课程中具体讲解。


# 方式一:
#     1、打开            打开文件  open(文件路径，访问模式)
#     2、读写数据    写入数据时，必须是字符串
#     3、关闭    关闭文件，如果不关闭。文件会始终保留在内存中，无法让内存及时回收（内存泄漏）

f = open('C:/Users/32022/Desktop/ww.docx', 'w', encoding='utf-8')
f.write('Oriya')
f.close()

# 方式二：自动关闭文件
#     优点：当执行完操作缩进内容时，会自动使用f来进行我呢见关闭操作

with open('123.txt', 'r', encoding='utf8') as f:
    print(f.read())


"""
    \x：称为转义字符   不会像普通字符输出，而是有特殊含义
            \t 辅助对齐
            \n 换行
        r"xx" 字符串前加r，表示将字符串中的所有内容都当作普通字符处理
    
        Windows 路径分隔符支持 / \
        Linux/macos 只支持 /
        建议使用 / 全系统兼容
    
        编码：人文语言 ——> 机器语言
        解码：机器语言 ——> 人文语言  编码解码不一致会乱码
        Windows中文版 文件读写时，默认使用gbk进行编码
    
    
    函数：print(self, *args, sep=' ', end='\n', file=None)
    print默认具有换行能力，可以设置end=''取消换行
    
    
"""

