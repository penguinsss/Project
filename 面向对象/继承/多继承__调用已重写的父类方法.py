class God:
    def eat(self):
        print('吃蟠桃')

    def drink(self):
        print('喝水')


class Dog:
    def eat(self):
        print('吃粑粑')

    def drink(self):
        print('喝牛奶')


class XTQ(Dog, God):
    # 需求：想要吃蟠桃 喝牛奶
    # 分析：此时，就不能通过改动继承顺序（继承链），改变顺序治标不治本
    # 解决方式：1> 重写
    #          2> 在重写的方法中调用父类的方法（调用被重写的方法）    父类.方法名（对象）
    def eat_drink(self):
        """
            此种写法调用的方法是 Dog对象类中的方法（因为本身没有，然后调用第一个父类Dog中的方法）
            self.eat()
            self.drink()
        """
        '''指定调用'''
        God.eat(self)
        Dog.drink(self)

        # 这种方式会从指定类在继承链中的下一个类开始查询
        # super(Dog, self).eat()  # 多继承情况下不建议使用


x = XTQ()
x.eat_drink()

# 查看继承链(方法查询顺序)
print(XTQ.mro())    # 类对象调用方法
print(XTQ.__mro__)


