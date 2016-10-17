# ----------------------------------
num = 1.1
count = 0

while num < 10:
    num *= num
    count += 1
print('1.1的', count, '次方大於10')

# -----------------------------------
num = 0.9
count = 0

while num < 10:
    num *= num
    count += 1
print('0.9的', count, '次方大於10')

# -----------------------------------
import random

score = random.randint(0, 100)
print('考試成績', score, '分')

# 只要成績小於60分就重考
while score < 60:
    score = random.randint(0, 100)
    print('考試成績', score, '分')

# -----------------------------------
# 只要成績小於60分就重考
while True:
    score = random.randint(0, 100)
    print('考試成績', score, '分')
    if score >= 60:
        break
