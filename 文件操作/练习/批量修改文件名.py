import os


def p():
    path = input('输⼊需要批量修改⽂件名的⽂件夹名称：')
    os.chdir(path)
    list_data = os.listdir()
    print(os.getcwd())
    print(list_data)
    for list_f in list_data:
        print(list_f)
        os.rename(list_f, '[复件]' + list_f)


p()
