class Item:
    def __init__(self, type, area):
        self.type = type
        self.area = area

    def __str__(self):
        return '类型：%s，属性：%s' % (self.type, self.area)


class Home:
    def __init__(self, address, area):
        self.address = address
        self.area = area
        self.free_area = area
        self.items = []

    def add(self, item):
        if self.free_area >= item.area:
            self.free_area -= item.area
            self.items.append(item)
            print('添加成功')
        else:
            print('添加失败')

    def __str__(self):
        return '地址：%s，占地面积：%s，剩余面积：%s，目前家中家具：%s' % (
        self.address, self.area, self.free_area, [item.type for item in self.items])


zz1 = Item('桌子1', 10)
zz2 = Item('桌子2', 300)
h = Home('西安', 300)
h.add(zz1)
h.add(zz2)
print(h)
