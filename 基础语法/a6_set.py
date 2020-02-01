'''set无序集合
    特点：无序 ； 去重'''
st = {1, 2, 5, 4, 2, 1, 6}
print(type(st), st)     # <class 'set'> {1, 2, 4, 5, 6}

# 文件读取中的一些隐藏问题 = tuple(st)
# print(type(文件读取中的一些隐藏问题))

t = (1,)
temp = set(t)
print(type(temp))















