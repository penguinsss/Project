i = 1
while i < 10:
    j = 1
    while j <= i:
        print('%s*%s=%s ' % (i, j, i * j), end='\t')   # 默认是每输出一个就换行
        j += 1
    i += 1
    if j == i:
        print()
