class Dog:
    # 方法中 既不需要实例对象， 也不需要类对象时，为了节省性能可将方法设为静态方法

    @staticmethod
    def eat():
        print('喝')


d = Dog()
d.eat()
Dog.eat()



# 静态方法: 方法中既不使用实例对象(修改/获取实例属性, 调用其他实例方法), 也不使用类对象(修改/获取类属性, 调用其他的类方法)
#          定义静态方法需要添加 @staticmethod， 对于参数没有要求
#           类中的函数
# 类方法:  方法中使用类对象(修改/获取类属性, 调用其他的类方法)
#         定义类方法需要添加 @classmethod， 并且至少有一个参数，默认参数名为cls， 代表调用该方法的类对象
# 实例方法:  方法中使用实例对象(修改/获取实例属性, 调用其他实例方法)
#           实例方法定义时，至少有一个参数，默认名为self，代表调用该方法的实例对象
