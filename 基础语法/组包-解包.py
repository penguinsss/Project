# 组包：等号右边有多个数据时，会自动包装为元组
t = 1, 'f', 5.1
print(t)

# 解包：变量数量 = 元素数量，元素会自动一一对应赋值
a, b, c = (1, 2.3, 5)
print(a)
print(b)
print(c)

a, b, c = [1, 2.3, 5]
print(a)
print(b)
print(c)

a, b = {'username':'星魂', 'password':'123321'}  # a = username  b = password
print(a)
print(b)


# 组包机制仅适用元组
# 解包机制元组、列表、字典均适用
#
#
# 应用场景：
#   交换两个变量的值；
a = 1
b = 2
a, b = b, a  #交换
print(a, b)

#   设置多个返回值；
def func():
    return 1, 2, 3
a0 = func()     # (1, 2, 3)
a, b, c =func()
print(a0)
print(a, b, c)

#   字典.items()
dict1 = {'name': '星魂', 'age': 12}
for item in dict1.items():
    print(item)

for key, value in dict1.items():
    print(key, value)

