list1 = [10, 20, 30, 40, 50]

# 遍历某个列表时, 最好不要对其进行元素的增删操作(增删操作可以改变元素的索引)
# for num in list1:
#     print(num)
#     if num == 30 or num == 40:
#         list1.remove(num)
#
# print(list1)


# 解决方案:
# 1> 遍历时, 只记录下来想要增删的元素(不立即增删)

temp_list = []  # 定义临时列表, 用于记录想要删除的元素
for num in list1:
    print(num)
    if num == 30 or num == 40:
        temp_list.append(num)

# 2> 等遍历完, 再进行增删操作
for temp_num in temp_list:
    list1.remove(temp_num)

print(list1)