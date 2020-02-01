# 需求：定义函数func_map，接收任意数量的数据，如func_map(1, 2, 3),返回列表，元素和数据的关系可以自定义
def p(n):
    return n ** 2


def c(n):
    return n ** 3


def func_map(*args, func_arg):
    return [func_arg(n) for n in args]
    # 文件读取中的一些隐藏问题 = []
    # for i in args:
    #     文件读取中的一些隐藏问题.append(func_arg(i))
    # return 文件读取中的一些隐藏问题


list_temp = func_map(1, 2, 3, 4, func_arg=p)
print(list_temp)




