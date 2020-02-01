class Fruits:  # 类名大驼峰

    def __init__(self, color, name):  # 使用场景：初始化
        self.color = color
        self.name = name

    def zd(self):  # self对应的实参是 调用该方法的对象（由解释器自动设置）；  使用场景：想在方法中使用对象自己的属性
        print('我长大啦')
        print("我是：%s" % self.name)

    def __str__(self):
        return '颜色：%s，名字：%s' % (self.color, self.name)


apple = Fruits('红红', '苹果')
apple.taste = '香甜可口'  # 属性：首次赋值会定义，再次赋值修改；  这种定义属性方式叫动态绑定
print("%s的%s" % (apple.color, apple.name))
print(apple.zd())

banana = Fruits('黄色', '香蕉')
print(banana.zd())

print(apple)


#   _xxx_(self):这类方法会在特定情况下自动调用，人称 '魔法方法'
#       ● __init__(self):对象一创建完自动调用，用于初始化处理
#       ● __str__(self):自定义对象的打印；
#                     必须有返回值，返回的内容会代替默认的对象打印（默认打印对象内存地址）
#       ● __del__(self):对象销毁前执行；
#                     1> 回收资源； 关闭文件、数据库连接等；
#                     2> 用户观察对象的删除情况（进行分析）；
#                    ★对象   局部变量  方法结束时销毁 ，执行_del_方法；
#                            全局变量  文件执行结束时 ，执行_del_方法；
#       ● __dict__(self):python编译器内部会将私有属性变量转为 '_类名和私有属性名'的字符串拼接，然后进行操作，所以在外部直接进行修改是改不了的
#       ● 查看继承链（方法查询顺序）  多继承:
#                   1> 属性： 类对象._mro_
#                   2> 方法： 类对象.mro()
#       ● __all__: 该变量可以控制 from 模块 import * 导入的内容
#                   如果不把功能放到__all__变量列表中，那么通过 ' from 模块 import * '导入时，是不会被导入的
#       ● __name__: ❀ 无论采用哪种导入方式，都会将模块中的代码全部执行一遍
#                     当主动执行模块文件时，__name__变量为__name__
#                     当模块被其他文件按导入时，__name__变量为 模块名
#                   if __name__ == '__main__':
#                         测试代码

class Dog:
    def __init__(self):
        self.file = open('123.txt', 'w')
        print(self.file)

    def __del__(self):
        print('对象销毁前回收')
        self.file.close()  # 对象删除前将文件关闭，避免内存泄漏


# python中 数字(int、float)、字符串(str)、列表(list)、函数(function) 都是对象
tuple1 = (1,)
list1 = list(tuple1)  # 强转 / 对象调用
print(type(list1))


# 私有属性： __xx
#           只能在类内部使用
#          在类外部使用会报错
#          即使强制在类外部赋值，私有属性值也不会修改
class Dog:
    def __init__(self):
        self.file = open('123.txt', 'w')
        self.__count = 1

    def __del__(self):
        print('对象销毁前回收')
        self.file.close()  # 对象删除前将文件关闭，避免内存泄漏（不及时释放从而造成内存空间的浪费）


d = Dog()
d._Dog__count = 4
print(Dog.mro())


# 私有方法：仅在类内部使用
































