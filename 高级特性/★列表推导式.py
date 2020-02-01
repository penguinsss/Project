"""
列表推导式：快速生成列表元素的表达式（一行）
格式：[计算公式 for循环]
    特点：
        1>每循环一次就按照计算公式的结果向列表中添加一个元素；
        2>计算公式可以使用for循环遍历出的数据
"""
list0 = []
for i in range(100):
    list0.append(i + 1)
print(list0)

list0 = [i + 1 for i in range(100)]
print(list0)

# 列表中包含1-100的偶数
list1 = [i for i in range(2, 101, 2)]
print(list1)

list1 = [i for i in range(1, 101) if i % 2 == 1]
print(list1)

# 练习
def str_0(list_0):
    return [temp for temp in list_0 if len(temp) > 4]


list3 = ['hello', 'boy', 'girl', 'apple', 'python']
print(str_0(list3))
