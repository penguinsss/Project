info_tuple = ('星魂', '14', 1.75)
print(info_tuple[0])

# 元组中 只包含⼀个元素 时，需要 在元素后⾯添加逗号，不然，元素类型会自动推导，不保留元组类型，
name = (1, )
print(name[0])

# 查询       元组[索引]             根据索引取值，索引不存在会报错
#           len(元组)              元组⻓度(元素个数)
#           if 值 in 元组:         判断元组中是否包含某个值
#           元组.index(值)         根据值查询索引，返回 第⼀个匹配项 的索引，没有查到会报错
#           元组.count(值)         值在元组中出现的次数


# 使⽤ `tuple` 函数 把列表转换成元组
list1 = [10, 11]
tuple1 = tuple(list1)
print(tuple1, type(tuple1))

# 使⽤ `list` 函数 把元组转换成列表
list1 = list(tuple1)
print(list1, type(list1))

# 元组使用场景：
#   1>列表转为元组，避免数据被修改
#   2>格式化操作（多个占位）








