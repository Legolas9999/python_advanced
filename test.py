# 请编写一个正则表达式，用于匹配符合以下要求的手机号码：

# 11位数字
# 第一位为1
# 第二位为3、4、5、6、7、8、9之一

import re

def find_matches(words, pattern):
    matches = []
    for word in words:
        if re.search(pattern, word):
            matches.append(word)
    return matches

# 示例字符串列表
words = ['apple', 'banana', 'cat', 'dog', 'elephant', 'fish']

# 需求1：搜索包含a或者e，并且后面跟了6个任意字符的元素
pattern1 = r'[ae].{6}'
matches1 = find_matches(words, pattern1)
print("需求1匹配结果:", matches1)

# 需求2：搜索以a或者e起始，后面跟了6个任意字符的元素
pattern2 = r'^[ae].{6}'
matches2 = find_matches(words, pattern2)
print("需求2匹配结果:", matches2)


