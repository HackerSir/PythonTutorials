"""
https://docs.python.org/3/library/functions.html#print
"""

# 單引號和雙引號都可以
print('hello, world')
print("hello, world")

# 多個字串，預設用空白分隔
print('aaa', 'bbb', 'ccc')

# 用 | 分隔
print('aaa', 'bbb', 'ccc', sep='|')

# 改變結尾符號
print('aaa', end='')
print('bbb')

print('aaa', end=',')
print('bbb')

a = "hello, "
b = "world"
print(a, b)
print(a + b)

year = 5
# 會發生錯誤的寫法 print(year + 5 + "aaaa")
print(year + 5, "aaaa")
print(str(year + 5) + "aaaa")

print("*" * 5)
