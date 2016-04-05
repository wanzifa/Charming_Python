#coding:utf-8
"""
闭包的概念:
一个可以引用在函数闭合范围内变量的函数
假如在一个外部函数中嵌套了一个内部函数
并且这个内部函数又引用了外部函数作用域里的变量
那么这个内部函数连带外部作用域一起，就叫做闭包。
"""
def counter(start_at=0):
    count = [start_at]
    def incr():
        count[0] += 1
        return count[0]
    return incr

a=counter(1)
print a()
b=counter(100)
print b()

