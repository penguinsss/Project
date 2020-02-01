class Animal(object):
    def __init__(self):     # 此时的self == Cat的实例对象tom
        self.name = "Tom"


class Cat(Animal):
    def __init__(self):
        # 一旦重写了init方法, 父类的init方法将不会调用, 父类定义的属性也不会继承
        # 这种情况下, 想要继承父类的属性, 需要手动调用父类的init方法 (调用被重写的方法)
        Animal.__init__(self)   # super().__init__()，相较而言，Animal.__init__(self)更好理解些
        self.color = "red"

    def __str__(self):
        return "my name is %s，my color is %s" % (self.name, self.color)


tom = Cat()
print(tom)

print('❀-------------------------')


class Dog:
    def __init__(self, type):
        self.type = type


class XTQ(Dog):
    def __init__(self, type):
        # super().__init__(type)
        Dog.__init__(self, type)    # 此方式必须要传两个参数
        self.color = '黑'


xtq = XTQ('天狗')
print(xtq.type)


print('❀-------------------------')


class Dog:
    def __init__(self, type_arg):
        self.type = type_arg
        print(type(self))  # 获取对象类型


class XTQ(Dog):
    def __init__(self, type):

        # 调用父类的init方法( ★继承属性 )
        Dog.__init__(self, type)

        self.color = '黑'


# dog1 = Dog('狗')  # 打印的对象类型为Dog
xtq = XTQ('天狗')  # 打印的对象类型为XTQ