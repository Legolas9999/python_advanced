import re

# 匹配字符串中连续出现的两个相同的单词
# 使用场景：只想要匹配到的内容的一部分
# 分组的编号从1开始
str1 = 'abcdef1111ghij2222klm2222n'
result = re.finditer(r'(\d)\1\1\1', str1)
#print(result.group())   # 匹配到的内容123
#print(result.group(1))  # 获取1号分组的内容
#print(result.group(2))  # 获取2号分组的内容

for i in result:
    print(i.group())