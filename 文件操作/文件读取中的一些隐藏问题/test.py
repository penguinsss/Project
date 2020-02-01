# 一般的读取方案
with open('./1.txt', 'r') as f:
    while True:
        d = f.readline()
        print(d, end='')
        if len(d) == 0:
            break
