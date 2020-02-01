import random

list_nums = []
for i in range(100):
    n = random.randint(1, 100)
    while list_nums.count(n) != 0:
        n = random.randint(1, 100)
    list_nums.append(n)
print(list_nums)


def bubble_sort(list_arg):
    for i in range(len(list_arg) - 1):
        for j in range(len(list_arg) - i - 1):
            if list_arg[j] > list_arg[j + 1]:
                temp = list_arg[j]
                list_arg[j] = list_arg[j + 1]
                list_arg[j + 1] = temp
    print(list_arg)


def select_sort(list_args):
    for i in range(len(list_args) - 1):
        min_index = i
        for j in range(i + 1, len(list_args)):
            if list_args[j] < list_args[min_index]:
                min_index = j
        if i != min_index:
            temp = list_args[i]
            list_args[i] = list_args[min_index]
            list_args[min_index] = temp

    print(list_args)


def insert_sort(list_arg):
    for i in range(1, len(list_arg)):
        index = 0
        temp = list_arg[i]
        for j in range(i - 1, -1, -1):
            if list_arg[j] > temp:
                list_arg[j + 1] = list_arg[j]
            else:
                index = j + 1
                break
        list_arg[index] = temp

    print(list_arg)


def partition(list_arg, left, right):
    value = list_arg[left]
    i = left
    j = right
    while i < j:
        while (i < j) and (list_arg[j] >= value):
            j -= 1
        list_arg[i] = list_arg[j]
        while (i < j) and (list_arg[i] <= value):
            i += 1
        list_arg[j] = list_arg[i]
        list_arg[i] = value
    return i


def quick_sort(list_arg, left, right):
    if left < right:
        p = partition(list_arg, left, right)
        quick_sort(list_arg, left, p - 1)
        quick_sort(list_arg, p + 1, right)
    return list_arg


if __name__ == '__main__':
    bubble_sort(list_nums)  # 冒泡
    select_sort(list_nums)  # 选择
    insert_sort(list_nums)  # 插入
    print(quick_sort(list_nums, 0, len(list_nums) - 1))
