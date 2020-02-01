# 模块中的 函数 全局变量 类
# 导入方式一: import 模块名
#           模块名.功能
# 导入方式二: from 模块 import */功能1，功能2，...
#           直接使用功能


# import test
import sys

from test import a, Dog    #❀ a, Dog 是新建的变量，指向了需要导入变量指向的地址

# 导入方式二中的陷阱
"""
    陷阱1：导入多个模块中的同名内容，后者会覆盖前者
            解决办法：取别名
                from test1 import a as test1_a
                from test2 import a as test2_a
    陷阱2：对导入的内容进行修改，不会使模块中的内容发生变化
            解决办法：一般不会对导入的变量进行赋值（如果需要赋值，使用类属性/实例属性来代替）
"""
import test
test.a = 10
test.func1()


# 模块查询路径，可将指定的目录添加到查询路径中，那么，该目录中的模块就可以被导入
print(sys.path) # 项目目录  解释器目录  第三方包的安装目录


''' ❀ 无论采用哪种导入方式，都会将模块中的代码全部执行一遍 '''
















