# parameter 形参  argument 实参
# 实参类型:  位置实参  关键字实参(命名参数)
# 形参类型: 普通形参  默认形参(缺省参数)  可变形参

# 位置实参: 普通实参   按照位置顺序赋值给形参, 要求和形参一一对应
def func1(num1, num2):
    print(num1)
    print(num2)


# func1(1, 3)


# 关键字实参: 可以将实参赋值给指定的形参
# 关键字实参必须在位置实参的后边
# func1(num2=1, num1=3)
