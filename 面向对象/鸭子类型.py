# 动态语言没有类型限制
# 设计模式是由于类型的限制造成的，所以python中是没有设计模式的

class Meat:
    def __init__(self):
        self.name = '肉'


class Tudou:
    def __init__(self):
        self.name = '土豆'


def eat(meat):
    print('吃：%s' % meat.name)


eat(Meat())
eat(Tudou())
