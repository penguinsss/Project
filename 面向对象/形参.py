# parameter 形参  argument 实参
# 实参类型:  位置实参  关键字实参(命名参数)
# 形参类型: 普通形参  默认形参(缺省参数)  可变形参(不定长参数)

# 默认形参: 可以形参设置默认值  设置实参则使用实参,不设置则使用默认值
# 默认形参必须在普通形参的后边
# def func1(num1, num2=10):
#     print(num1)
#     print(num2)
#
#
# func1(1)


"""可变形参: 元组型 和 字典型"""

# 元组型可变形参: 可以接收任意数量的位置实参
# 格式:  在形参前加* 表示该形参为 元组型可变形参
# 机制:  可以将任意数量的位置实参包装为元组, 再赋值给可变形参args

# def func_sum(*args):  # args = (1, 2, 4, 5)
#     """求和函数"""
#     sum = 0
#     for num in args:
#         sum += num
#
#     print(sum)


# 需求: 接收任意数量参数进行求和
# func_sum(1, 2, 4, 5)
# func_sum(1, 2)


# 字典型可变形参: 可以接收任意数量的关键字实参
# 格式: 在形参前加** 表示该形参为 字典型可变形参
# 机制: 可以将任意数量的关键字实参包装为字典, 再赋值给形参kwargs


# def save_userinfo(name, age, height, weight, gender):
def save_userinfo(name, **kwargs):
    print(name)
    print(kwargs)  # 字典
    # print(kwargs.get('age'))
    # print(kwargs.get('height'))


save_userinfo('张三', age=20)
save_userinfo('张三', height=1.7, weight=75, gender=True)
