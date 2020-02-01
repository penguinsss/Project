class Dog:
    def bark(self):
        print('汪汪叫')


class XTQ(Dog):
    def bark(self):
        print('嗷嗷叫')

    def see_host(self):
        print('摇尾巴')
        # self.bark()  # 重写了bark方法, 调用的一定是自己的bark方法

        # 需求: 调用父类的bark方法 (调用被重写的方法)   三种语法
        # 语法1  父类.方法名(对象)
        Dog.bark(self)

        # 语法2 super(当前类, 对象).方法名()
        # super(XTQ, self).bark()

        # 语法3 super().方法名()   语法2的简化形式    使用率最高
        # super().bark()


xtq = XTQ()
# xtq.bark()
xtq.see_host()
print(XTQ.__dict__)
