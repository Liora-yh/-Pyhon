"""
Python中正则表达式使用re模块，并基于re模块中三个基础方法来做正则匹配
分别是：match、search、findall三个基础方法
"""
import re


# re.match(匹配规则, 被匹配的字符串)
# 从被匹配的字符串开头进行匹配，匹配成功返回匹配对象（包含匹配信息），不成功返回空
s = 'python itheima python itheima python itheima'

result = re.match('python', s)
print(result)
print(result.span())    # (0, 6)
print(result.group())

s1 = '1python itheima python itheima python itheima'
result = re.match('python', s)
print(result)   # None


# re.search(匹配规则, 被匹配的字符串)
# 搜索整个字符串，找出匹配的，从前向后，找到第一个后，就停止，不会继续向后
# 整个字符串都找不到，返回None
str = '1python666itheima66python666'
result1 = re.search('python', str)
print(result1)
print(result1.span())    # (1, 7)
print(result1.group())


# re.findall(匹配规则, 被匹配的字符串)
# 匹配整个字符串，找出全部匹配项，找不到，返回空list:[]
str2 = '1python666itheima66python666'
result2 = re.findall('python', str2)
print(result2)

str3 = '1python666itheima66python666'
result3 = re.findall('itcast', str3)
print(result3)      # []