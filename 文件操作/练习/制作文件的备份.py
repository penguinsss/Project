# 需求：输⼊⽂件的名字，然后程序⾃动完成对⽂件进⾏备份
def copy():
    in_str = input('请输⼊拷⻉⽂件名：')
    with open(in_str) as f:
        content = f.read()
    new_str = in_str.replace('.', '[复件].')

    # dot_index = in_str.rfind('.')
    # new_str = in_str[:dot_index] + '[复件]' + in_str[dot_index:]

    with open(new_str, 'w') as f:
        f.write(content)


copy()
