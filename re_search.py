#coding:utf-8
"""
这里涉及到两个小点
search()用法和match用法的区分
前者匹配整个字符串 出现匹配的就返回
后者不然 只匹配一开始的 字符串起始位置匹配不上 那就再见吧
另一个点就是 ()在这里，是给匹配结果分组的意思
不是很复杂的知识点 但是很重要
"""

import re
text = "JGood is a handsome boy, he is cool, clever, and so on..."
m = re.search(r'\shan(ds)ome\s', text)
n = re.match(r'\shan(ds)ome\s', text)
if m:
    print '分组后输出为:{0},{1}'.format(m.group(0),m.group(1))
    print '整个组输出为:{0}'.format(m.groups())
else:
    print 'search失败啦'
if n:
    print 'match成功啦'
else:
    print 'match失败啦'


