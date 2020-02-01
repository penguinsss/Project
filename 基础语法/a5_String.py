# 字符串的定义方式一：
s0 = 'hellhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhho'
print(s0.rfind('o'))    # 只要没值就返回-1，有值只会返回正数

# 字符串的定义方式二：
s1 = '''    阴阳家
星魂大人
盖聂
月儿
'''
print(s0, s1, type(s1))

print('.........')

# 引号的使用，转义字符的使用
s2 = "hello 'py'thon"
s3 = "he\nllo \"py\"thon"
print(s2)
print(s3)

'''根据索引取出字符'''
s_t = 'username'
print(s_t[0])

'''遍历'''
for c in s_t:
    print(c)

print('........')

ss = 'hello python'
'''查找   find默认从左到右，返回第一个匹配的索引
          find查找，查到返回其索引，返回的索引表示方式使用的是正数，即结果要么大于0，要么查不到返回-1
          rfind和find一样，不过它是从右边开始查
          find(内容，开始索引，结束索引)  在索引范围内查找，结尾可以不设置  🔺左闭右开'''
index1 = ss.find('w')
index2 = ss.find('o')
index3 = ss.rfind('o')
index4 = ss.find('o', -3, -2)
print(index1, index2, index3, index4, '。。。。。。。。。。。')

my_string = 'helloJavahellopythonhelloc++helloc'
print(my_string.find('hello'))

'''替换
    replace(旧内容，新内容，替换次数)  用新内容替换旧内容，返回替换后的新字符串（原字符串不变）
    可以指定替换次数，默认全部替换'''
ss0 = ss.replace('o', '9', 1)
ss1 = ss.replace('python', 'Java')
print(ss, ss0, ss1)

print('.........')

'''拆分，拆分结果是列表'''
ss2 = 'hello python world'
result1 = ss2.split(' ')
result2 = ss2.split(' ', 1)     # 指定拆分次数
print(result1, result2)

'''拼接，join拼接效率更高些'''
# 加号拼接
city1 = '南京'
city2 = '上海'
result3 = city1 + city2
print(result3)

# 连接符.join(可迭代对象：可以进行for循环便遍历的数据)
join_str = '*'
result4 = join_str.join([city1, city2, '西安'])   # 该方法要求的可迭代对象中元素必须是字符串
print(result4)



'''★切片   使用最多, 前提是有序        字符串（用的比较多）、列表、元组都支持切片★
    切片格式：字符串[开始索引：结束索引]  🔺左闭右开
                省略开始索引表示从头开始取到结束索引
                省略结束索引表示从开始索引截取直到最后
    切片也支持负数索引
    步长公式：当前索引 + 步长 = 下一个数据的索引'''
s4 = 'hello yatou~'
print(s4[0:5])  # hello
print(s4[0:-5])     # hello y
print(s4[::-2])     # ~oa le
print(s4[11:-7:-1])   # ~uotay
print(s4[-1:-2:-1])     # 最常用，将字符串翻转

str1 = 'hellopython'
print(str1[:3:-2])  # nhyo

# 练习：将输入的文件名 123.txt -> 修改为123[附件].txt
file_name = input('请输入文件名：')
new_file_name1 = file_name.replace('.', '[附件].')

index = file_name.rfind('.')
print(index)
new_file_name2 = file_name[:index] + '[附件]' + file_name[index:]
print(new_file_name1, new_file_name2)











