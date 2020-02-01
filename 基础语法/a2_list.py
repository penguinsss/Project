# 列表 列表中的元素类型不限
name_list = ['东皇太一', '星魂', '东皇太一', '大司命', '少司命', '雪女', '高渐离', '天明', '月儿']
print(name_list[-8])
print(name_list[0])


print(name_list)
# 嵌套
name_list1 = [
    ['阴阳家', '儒家', '墨家', '法家', '道家', '流沙'],
    ['东皇太一', '星魂', '少司命', '大司命'],
    ['雪女', '高渐离', '天明', '月儿', '盖聂'],
    ['韩非'],
    ('a', 's')
]
print(name_list1[0][0] + name_list1[1][0])
print(name_list1[-1])

#
# 分类          关键字/函数/⽅法             说明
# 增加          列表.append(值)            在末尾追加值
#               列表.extend(可迭代对象)    将可迭代对象 中 的元素 追加到列表
#               列表.insert(索引, 值)      在指定位置插⼊值, 超过索引会追加值
# 删除          列表.remove(值)            删除指定值的 第⼀个匹配项；想要删的值不存在报错；想要删除所有遍历删除，需要借助另外一个列表存储想要删除的元素
#               del 列表[索引]             删除指定位置的值；数组越界报错
#               列表.pop(索引)             删除指定索引的值, 并返回被删除的值；数组越界报错；不传索引默认删除最后一个元素
#               列表.clear()               清空列表
# 修改          列表[索引] = 值            修改指定索引的值，索引不存在会报错
# 查询          列表[索引]                 根据索引取值，索引不存在会报错
#               len(列表)                  列表⻓度(元素个数)
#               if 值 in 列表:             判断列表中是否包含某个值
#               列表.index(值)             根据值查询索引，返回 第⼀个匹配项 的索引，没有查到会报错；值不存在也会报错
#               列表.count(值)             值在列表中出现的次数
# 排序          列表.sort()                排序(升序)       列表.sort(reverse = True)（倒序）
#               列表.reverse()             逆序、反转
#

print('..........................')

name_list.sort()
print(name_list)

name_list.reverse()
print(name_list, name_list.count('东皇太一'))

print('..........................')
print(name_list, len(name_list))
name_list.insert(0, '文文')
print(name_list, len(name_list))

name_list.extend(name_list1)
print(name_list)

# 遍历
for name in name_list:      # 会先根据索引顺序尝试取元素，然后判断该元素是否可以取出
    print(name)             # 如果可以取出，将取出的值赋值给变量，并执行循环体中的代码
print(name)


# 练习
list1 = []
while True:
    n = input('请输入要操作的编号：1.添加姓名 2.删除姓名 3.显示全部姓名 4.退出程序')
    if n == '1':
        name = input('请输入想要添加的姓名：')
        list1.append(name)
        print('姓名添加成功')
    elif n == '2':
        name = input('请输入想要删除的姓名：')
        if name in list1:
            for name in list1:
                list1.remove(name)
            print('删除成功')
        else:
            print('不包含{0}', name)
    elif n == '3':
        if len(list1) == 0:
            print('此列表为空')
        else:
            for n in list1:
                print(n)
    elif n == '4':
        print('退出程序')
        break
    else:
        print('输入有误, 请重新输入')



print(list(range(10)))












































