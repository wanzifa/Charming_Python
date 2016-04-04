#coding:utf-8
"""
Python中的生成器
"""

#先来看一个最简单的
simple_g = (x*x for x in range(10))
print '生成器示例simple_g的输出为：{0}'.format(simple_g)
# 不出所料的话，输出结果会是一个对象类型，而不是列表
# 锵锵锵！为啥呢？
# 这个看起来和列表很像又和元组很像的东西 和它们可没什么关系哈
# 这个东西 叫做生成器解析式子
# 当它作为参数传入时，甚至不需要加括号
sum_g = sum(x for x in range(10))
print '生成器解析式作为参数传入的示例中，0到9的和顺利输出：{0}'.format(sum_g)

"""
下面深入剖析生成器
生成器的标志 是yield
有生成器的地方 内部就有yield
换句话说 如果一个对象内部引入了yield
那么它将成为一个生成器"""
# 生成器解析式返回的生成器对象中 
# 每调用一次next()方法 
# 其实内部都伴随一次yield函数的执行
print "生成器的执行过程，输入simple_g.next()后返回：{0}".format(simple_g.next())

"""
生成器与外界的数据交流
"""
def test(n):
    while True:
        n = yield n
# 在第一次yield执行完毕后 n变成空了
# 此时如果继续调用yield 什么也不返回
# 通过send()方法可以向n赋值 然后yield会继续执行 返回相应的值
test_g = test(4)
print 'test函数第一次返回的值为：{0}'.format(test_g.next())
print 'test函数经用户输入n值后返回的值为:{0}'.format(test_g.send('hello'))



