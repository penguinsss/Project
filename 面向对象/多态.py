# 多态： 让同类的对象呈现多种表现形式（子类化）
#       方便项目代码升级和重构

"""
    先继承
    然后实现该'接口'方法
    父类的引用指向子类的对象，从而调用子类的实现类
"""


class Person:
    def dance(self):
        pass

    def play(self):
        self.dance()


class OldMan(Person):
    def dance(self):
        print('跳广场舞')


class Baby(Person):
    def dance(self):
        print('蹦蹦跳')


OldMan().play()
Baby().play()
