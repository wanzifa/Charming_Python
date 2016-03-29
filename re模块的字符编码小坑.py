#coding:utf-8
"""
今天读代码的时候遇到一种没见过的re模块compile函数的用法
compiled_regex = re.compile(regex, re.UNICODE)
心想这第二个参数re.UNICODE是什么鬼！
究竟是什么鬼 大家且看我以身试法！
"""

#这一行用我们最常见的那种用法
pattern = re.compile(ur"a\s+b")
# 注意\u3000是unicode编码中的空格
# 所以按理说是可以匹配的嘿嘿
m = pattern.findall(u"dsadadsada\u3000b") 
#看看会输出什么?
print m

# 不出意外的话 输出的是空列表
# 为什么？
# 试试re.UNICODE吧！
pattern = re.compile(ur'a\s+b', re.UNICODE)
m = pattern.findall(u"dsadadsada\u3000b")
print m

"""
总结
这个参数表明正则表达式匹配时遵循的编码规范
如果我指定了re.UNICODE 
就意味着前面的正则表达式编译出的对象要按照UNICODE的编码规范去匹配字符串
\u3000对应UNICODE编码中的空格，但不对应str编码中的空格
但是我们第一次没有指名第二个参数 于是它默认按照str编码规范编译了正则表达式
当然匹配不到啦!
"""

