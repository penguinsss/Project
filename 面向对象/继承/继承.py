"""
    继承：拥有父类的属性和方法     系统方法是不会继承的，比如：print()方法
    私有属性和方法不被继承，

"""


class Animal:
    def eat(self):
        print('吃')
    print('。。。。。。。')


class Dog(Animal):
    def bark(self):
        print('叫')

    print('*****')


class XTQ(Dog):  # 支持多层继承
    pass


x = XTQ()
x.bark()
x.eat()




