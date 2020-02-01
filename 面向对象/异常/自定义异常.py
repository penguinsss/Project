"""
    1.继承BaseException
    2.在需要进行处理的位置，主动抛出异常
        格式：raise 异常对象
    3.在代码的外侧对自定义异常进行捕获，以便进行统一的异常处理，减少代码的冗余
"""


# 封装异常处理   有利于代码重构（一改都改，方便修改）
class PhoneNumError(BaseException):
    def handle_error(self):
        print('显示弹窗')
        print('提示：出现手机号错误 %s' % self)
        print('关闭弹窗')


try:
    phone_num = input('请输入手机号：')
    if len(phone_num) != 11:
        raise PhoneNumError('位数错误')
    elif not phone_num.isdecimal():  # isdecimal() 判断字符串是否都是数字，是返回True，否返回False
        raise PhoneNumError('含有非数字')

except PhoneNumError as e:  # e是抛出的异常对象（eg.PhoneNumError('位数错误')）
    e.handle_error()
