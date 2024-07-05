import re
# 2、匹配任意某1个字符
str2 = '@abcd1234'
result = re.findall('\d{3,}', str2)

print(result)