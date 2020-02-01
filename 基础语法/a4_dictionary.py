# 字典：没有索引，是无序的
#   值 任何数据类型
#   键 字符串、数字或 元组

# 定义字典
ww = {"name": "⼩明", "age": 18, "height": 1.75}  # RuntimeError: dictionary changed size during iteration
print(ww["name"])


# 分类          关键字/函数/方法                        说明
# 增加          字典[键] = 值                       键不存在，会添加键值对
# 删除          字典.pop(键)                        根据键删除键值对,返回被删除的值   不存在时报错，可添加一个默认值参数就不报错了
#               del 字典[键]                        根据键删除键值对
#               字典.clear()                        清空字典
# 修改          字典[键] = 值                        键存在，会修改键值对的值
#               字典.setdefault(键，数据)           键值对不存在，添加键值对；存在则不做处理
#               字典.update(字典2)                  取出字典2的键值对对字典1操作，键值对不存在，添加键值对；存在则修改值
# 查询          字典[键]                           根据键取值，键值对不存在会报错
#               字典.get(键)                         根据键取值，键值对不存在返回None, 不会报错
#               for key in 字典                     遍历字典, 获取所有的键
#               for key in 字典.keys()              遍历字典, 获取所有的键
#               for value in 字典.values()          遍历字典, 获取所有的值
#               for item in 字典.items()            遍历字典, 获取所有的键值对 (键, 值)  元组形式

'''新增，键已经存在修改，不存在新增'''
dict1 = {'name': '星魂', 'age': 12, 'color': '紫色', 'height': 1.8}
print(dict1, 'name' in dict1)

print('99999999999')
print(type(dict1))

print('.............')

'''删除，del删除键不存在时会报错
         pop删除键不存在时可设置默认值避免报错'''
print(dict1.pop('colors', 'no keys') + '。。。。。。。。')

del dict1['name']
print(dict1)

print('.............')

'''查询，通过下标取值键不存在报错
         get取值会返回none不报错'''
print(dict1['age'])
print(dict1.get('height'))

print('.............')

'''遍历'''
print(',,,dict1')
for key in dict1:
    print(dict1[key])

print(',,,dict1.keys()')

for key in dict1.keys():
    print(dict1[key])

print(',,,dict1.values()')

for value in dict1.values():
    print(value)

print(',,,dict1.items()')

for item in dict1.items():
    print(item[0])

# 练习
list_dict = []    # 此处除了定义为列表且列表元素为字典外，还可以采用字典包裹字典，不过这个外层字典的键取值时需要考虑其一唯一性，其二便捷，便于后续代码的编写
while True:
    n = input('请输入操作：1.用户注册 2.用户登录 3.查询用户信息 4.退出程序')
    if n == '1':
        dict1 = {}
        username = input('请输入用户名：')
        password = input('请输入密码：')
        age = input('请输入年龄：')
        dict1['用户名'] = username
        dict1['密码'] = password
        dict1['年龄'] = age
        list_dict.append(dict1)
        print('新增成功')
        print(list_dict)
    elif n == '2':
        username1 = input('请输入用户名：')
        password1 = input('请输入密码：')
        for dict_t in list_dict:
            if dict_t['用户名'] == username1 and dict_t['密码'] == password1:
                print('登录成功')
                break                                            # ★ break和else互斥执行，for循环、while循环均适用
        else:
            print('登录失败')
    elif n == '3':
        username = input('请输入查询的用户名：')
        for dict_t in list_dict:
            if dict_t['用户名'] == username:
                print('用户名：' + username + ', 年龄：' + dict_t['年龄'])
                break
        else:
             print('查无此人')
    elif n == '4':
        break
    else:
        print('输入有误，请重新输入')















