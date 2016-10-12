num = 10

if num > 5:
    print('num > 5')

if num > 5:
    print('num > 5')
else:
    print('num <= 5')

if num > 5:
    print('num > 5')
elif num < 5:
    print('num < 5')

if 0 < num and num < 15:
    print('0 < num and num < 15')

# 沒錯，Python可以這樣寫，其他語言則不一定
if 0 < num < 15:
    print('0 < num < 15')

# 一種數線的寫法，我覺得可讀性比較高
if num < 0 or 15 < num:
    print('num < 0 or 15 < num')

if not num < 15:
    print('not num < 15')

# 縮排內需要程式碼，可以先暫時放 pass
if num < 5:
    pass

# 舉一反三，可以寫出複雜的 if
a = 5
b = 10
if a < 10:
    if b > 5:
        pass
    else:
        pass
elif a < 5:
    pass
else:
    pass
