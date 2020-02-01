# 函数名相当于变量名，而且还是一个全局变量，是一个代号，指向了这个函数
def fun():
    print('丫头')


a = fun
print(a())      # 丫头 \n None
print(fun())    # 丫头 \n None
print(a, fun)   # <function fun at 0x000001DEA6291048> <function fun at 0x000001DEA6291048>

print('。。。。。。。。。。。。。。求和、求差')


def func_sum(num1, num2):
    return num1 + num2


def func_sub(num1, num2):
    return num1 - num2


def fun_all(num1, num2, func_arg):
    ret = func_arg(num1, num2)
    print('运算结果为：%s' % ret)


fun_all(1, 2, func_sum)
fun_all(1, 2, func_sub)

'''
    要求定义函数可以对数据进行过滤，并可以自由指定过滤算法
'''


def func1(num):
    return num % 2 == 0


def func2(num):
    return num % 2 == 1


def func_filter(*args, func_arg):
    return [num for num in args if func_arg(num)]


data = func_filter(1, 2, 3, 4, 5, 8, 6, func_arg=func1)
print(data)
data = func_filter(1, 2, 3, 4, 5, 8, 6, func_arg=func2)
print(data)

print('。。。。。。。。')

'''
    引出：内置高阶函数filter
    python中将函数的参数为函数引用的函数称为高阶函数
    匿名函数可用于辅助高阶函数来使用
'''
data = filter(func1, [1, 2, 3, 4, 8])
for num in data:
    print(num)
data = filter(lambda num: num > 3, [1, 2, 3, 4, 8])
for num in data:
    print(num)


# （lambda 参数1，参数2：返回值）（实参1，实参2）
def func_filter(*args):
    return [num for num in args if (lambda num: num % 2 == 0)(num)]


print(func_filter(1, 2, 3, 4, 5, 8, 6))







