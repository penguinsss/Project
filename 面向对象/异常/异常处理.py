# 美观  功能强大  易用  稳定， 稳定性对于程序最重要
# 异常处理作用：   网络/用户等带来的一些可预判的错误进行提前的保护措施
#     提高程序稳定性
#     获取错误信息，用于分析问题


"""
    BaseException是异常类的基类
"""

#
# try:    # try后边except和finally至少要有一个，else可有可无，有else必须要有except
#     ...
# except:     # 出现异常走except
#     ...
# else:   # 没有异常走else
#     ...
# finally:    # 不论是否出现异常，都会走 finally
#     ...

""" 
    except: 这种格式可捕获所有错误 
    except 具体的异常类:
    except(异常类1，异常类2)：
"""
f = None
file_name = input('请输入文件名：')
try:
    f = open(file_name)
    content = f.read()
    print(content, type(f))
except BaseException as e:  # 打印具体的错误信息 ★
    print('出现错误：%s' % e)
finally:
    if type(f) == "<class '_io.TextIOWrapper'>":
        f.close()






















