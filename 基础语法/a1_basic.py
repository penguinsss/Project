import random, time
# 单行注释  快捷键：ctrl+/
print('星魂')


#  ▼
#    算数运算符：+    -   *    /   //:取整   %   **：次方
#
print(4//3)
print(4/3)
print(2**3)

# 变量  python严格区分大小写 eg:A a  python中变量：单词小写，多个单词间使用下划线；项目名使用大驼峰
name = '大司命'
print(name)

price = 8.5
weight = 7.5
total_price = price*weight
print(total_price)

#  ▼1
#     数据类型 ：数字、非数字      ★变量类型由解释器自动识别 （动态语言,js,好处：灵类型活随时可以改,缺点：不容易找错） Java/C:静态语言
#         数字：int
#               float  注意：浮点数运算可能出现精度缺失情况：原因是浮点数转为二进制时出现无限循环的情况
#                      开发过程中对于这一问题的解决方式：
#                      round(原数据,位数) 四舍五入
#                      eg:round(62.900001,3) ---- 62.9
#               bool(true 1 False 0)
#               int、float、bool这3个可直接进行运算
#               complex（复数型） 矩阵
#         非数字：str  可参与两种两种运算：
#                      +：字符串的拼接
#                      字符串*整数：表示重复的拼接，eg. hj*3
#                 列表
#                 元组
#                 字典
#     type()：查看数据类型


name = '高渐离'
age = 22
gender = True
height = 175.5

height = 'hh'
print(type(height))
print('hj'*3)
print('over')

# ▼2
#     格式化：      ♥是对字符串进行的操作，和print没有直接关系♥
#         常⽤格式化字符    含义
#            %s          字符串   ★可对应任何类型，会自动保留小数位数
#             %d          有符号⼗进制整数， %06d 表示输出的整数显示位数，不⾜的地⽅使⽤ 0 补全
#             %f          浮点数， %.2f 表示⼩数点后只显示两位
#             %%          文本输出 %
#         print("我的学号是 %06d" % student_no)
#         print("苹果单价 %.02f 元／⽄，购买 %.02f ⽄，需要⽀付 %.02f 元" % (price, weight, total_price))
#                                                                     ☆(price, weight, total_price) python中这叫元组

stu_num = 10
print('格式化字符串：%13d' % stu_num)  # 整数占3位，不足空格填充
print('格式化字符串：%d' % stu_num)
print('格式化字符串：%03d' % stu_num)  # 整数占3位，不足0填充，补数据只对0有效

f = 0.75
print("浮点数：%f" % f)
print("浮点数：%.2f" % f)
print("浮点数：%.02f" % f)

i = 1
print('学号：%05d' % i)

print('学号：{0}，姓名：{1}'.format('02152027','星魂'))

# ▼3 输入
# input()函数的返回值都是字符串
s = input('please enter your name：')
print(s)

# ☆注意：浮点数形式的字符串⽆法转换为int，如 int("1.5") 会报错
a = input('请输入一个整数：')
b= input('请输入一个整数：')
print(int(a)*int(b))

print(int(float('1.5')))

# ▼4
# 比较运算符：==    !=  >   >=  <   <=
# 字符串 和 数字 不能⽐较
# 字符串⽐较: "z" > "a" > "A" > "数字"

print('z' > 'Z')  # True
print('z' > '100000000000000')  # True 字母永远大于数字
print('ab' > 'ba')  # False 按位比，第一位比出来结果后边的就不必比较了

# ▼5
# 逻辑运算符：and or not
# and和or可参与运算

# 逻辑运算中的规则：
# and的返回结果：前者为真，返回后者；前者为假，返回前者
# or的返回结果：前者为真，返回前者；前者为假，返回后者

10 and 20 ------20
0 and 20 ------0
'' and 20 ------''
10 and 20 and ''------''

print(1 and 2)
print(1 or 2)

a = int(input('请输入您对您颜值的分数：'))
b = int(input('请输入您对您心灵的分数：'))
is_women = input('请输入您的性别：')
if a > 5 and b > 5:
    print('既有颜值心灵也美~')
if a > 5 or b > 5:
    print('有颜值或心灵美')
if not is_women == '男':
    print('女')


# ▼6 if判断
# 细节1:
# ① 数据如果时数字类型，则非0为真，0为假；
# ② 数据如果是字符串，有内容为真，无内容为假
# 细节2:
# 三目运算：条件成立时的语句 if 条件判断 else 条件不成立时的语句
# a > b ? 条件成立时的语句：条件不成立时的语句
print('允许进入网吧') if age >= 18 else print('不允许进入网吧')

age = int(input('请输入您的您的年龄：'))
if age >= 18:
    print('允许进入网吧')
else:
    print('不允许进入网吧')


if 'z' > 'Z':
    print('小写字母大于它相对应的大写字母')
elif 1 > 2:
    print('1 > 2')
else:
    print('小写字母小于它相对应的大写字母')
    print('哈喽，丫头~')


# ▼7 随机数 import random
#        random.randint(a, b) ，返回 [a, b] 之间的整数，包含 a 和 b
print(random.randint(12, 23))
print(random.randint(0, 1))

print('3'.isdigit())

# while循环
# 赋值运算符：=   +=  -=  /=  //= %=  **=
while 1 < 2:
    print('hello，world')
# 求和：
i = 0
sum_1 = 0
while i <= 100:
    sum_1 += i
    i += 1
print(sum_1)

# 秒表
h = 0
while h <= 23:
    m = 0
    while m <= 59: # 每⼩时,需要执⾏60次分针移动
        s = 0
        while s <= 59:  # 每分钟,需要执⾏60次秒针移动
            print("当前时间：%02d:%02d:%02d" % (h, m, s))
            time.sleep(1)
            s += 1
        m += 1
    h += 1


# break和continue只用于循环中, while或for










