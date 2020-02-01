my_str = 'hello world'
my_list = []
for i in my_str:
    if i != ' ' and i not in my_list:
        my_list.append(i)
        print('%s:%s' % (i, my_str.count(i)), end='\n')
print(my_list)








