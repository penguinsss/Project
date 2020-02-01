# 需求：保存用户信息，用户名、身高、年龄选填
info = {}


def dict(**d):
    global info
    dict1 = {}
    dict1['username'] = d.get('username', '未填写')
    dict1['height'] = d.get('height', '未填写')
    dict1['age'] = d.get('age', '未填写')
    info[d.get('username', '未填写')] = dict1


dict(username='星魂', height=1.75, age=14)  # 键最好使用英文
dict(username='东皇太一', height=1.8)
print(info)


def d(n):
    if n == 1:
        return 1
    else:
        return n ** 2 + d(n - 1)


def print_lines(char, len0, raw):
    for i in range(0, raw):
        print(char * len0)
    # i = 1
    # while i <= raw:
    #     print(char*len)
    #     i += 1


print_lines('。', 4, 3)
