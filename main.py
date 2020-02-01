import tools

while True:
    tools.show_menu()
    n = input('请选择执行的操作：')
    print('您选择的功能：' + n)
    if n == '1':
        tools.new_card()
    elif n == '2':
        tools.show_all()
    elif n == '3':
        tools.get_card()
    elif n == '0':
        print('欢迎再次使用[名片管理系统]')
    else:
        print('输入有误，请重新输入')







