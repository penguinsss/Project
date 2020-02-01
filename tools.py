card_dict = []


# 首页
def show_menu():
    print('*' * 30)
    print('欢迎使用[名片管理系统] V1.0')
    print()
    print('1.新建名片')
    print('2.显示全部')
    print('3.查询名片')
    print()
    print('0.退出系统')
    print('*' * 30)


# 新建名片
def new_card():
    print('功能：新建名片')
    name = input('请输入姓名：')
    age = input('请输入你年龄：')
    dict1 = {'name': name, 'age': age}  # 凑一块添加
    card_dict.append(dict1)
    print('添加名片成功')
    print(card_dict)


# 显示全部
def show_all():
    print('功能：显示全部')
    if len(card_dict) == 0:
        print('提示:没有任何名片记录')
        return  # ★
    print('姓名\t\t年龄')
    print('-' * 30)
    for dict0 in card_dict:
        print('%s\t\t%s' % (dict0['name'], dict0['age']))  # ★
    print('-' * 30)


# 查询名片
def get_card():
    temp = 0
    list0 = []
    print('功能：查询名片')
    name = input('请输入查询的姓名:')
    for dict0 in card_dict:
        if dict0['name'] == name:
            list0.append(dict0)
            temp = 1
    if temp == 0:
        print('没有找到%s' % name)
    else:
        print('-' * 30)
        for t in list0:
            print('%s\t\t%s' % (t['name'], t['age']))
        print('-' * 30)
        deal_card(list0)


# 名片高级处理
def deal_card(list0):
    while True:
        n = input('请输入对名片的操作：1.修改 2.删除 0.返回上一级')
        if n == '1':
            update_card(list0)
        elif n == '2':
            delete_card(list0)
        elif n == '0':
            break
        else:
            print('输入有误，请重新输入')


# 修改名片
def update_card(list0):
    name = input('请输入姓名：')
    age = input('请输入年龄：')
    for dict1 in list0:
        dict1['name'] = name
        dict1['age'] = age
    print('修改成功')


# 删除名片
def delete_card(list0):
    for d in list0:
        card_dict.remove(d)
    print('删除成功')
