"""
    匿名函数：没有名字的函数，它是 以表达式来    定义的简单函数
    定义格式：
        lambda 参数1， 参数2：返回值
    调用格式：
        （lambda 参数1，参数2：返回值）（实参1，实参2）
    优点：
        匿名函数调用完的内存就会回收；
        性能比普通函数要好一些
"""

print((lambda num1, num2: num1 + num2)(1, 2))

"""（lambda 参数1，参数2：返回值）相当于函数名"""
# 匿名函数的应用：
data = filter(lambda num: num % 2 != 0, [1, 2, 3, 4, 5])  # filter(__function, __iterable)
for num in data:
    print(num)

list1 = [['zs', 10], ['lisi', 33], ['ww', 8]]
list1.sort(key=lambda arg: arg[1])
print(list1)    # [['ww', 8], ['zs', 10], ['lisi', 33]]
