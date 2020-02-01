import timeit


def t1():
    li = []
    for i in range(10000):
        li.append(i)


def t2():
    li = []
    for i in range(10000):
        li = li +[i]


def t3():
    li = [i for i in range(10000)]


def t4():
    li = list(range(10000))


def t5():
    li = []
    for i in range(10000):
        li.insert(0, i)


time1 = timeit.Timer('t1()', 'from __main__ import t1')
time2 = timeit.Timer('t2()', 'from __main__ import t2')
time3 = timeit.Timer('t3()', 'from __main__ import t3')
time4 = timeit.Timer('t4()', 'from __main__ import t4')
time5 = timeit.Timer('t5()', 'from __main__ import t5')


print('append:%s' % time1.timeit(number=100))   # 0.127835
print('[]+[]:%s' % time2.timeit(number=100))         # 19.7184115
print('列表推导式:%s' % time3.timeit(number=100))      # 0.04835290000000114
print('list():%s' % time4.timeit(number=100))         # 0.026356299999999777
print('insert:%s' % time5.timeit(number=100))        # 2.6034982000000007
















