"""

逻辑结构

list
dict
判断 if elif else
break
continue
while
"""
list = [i for i in range(0, 10)]
print(list)

empty_list = []
for i in range(10):
    empty_list.append(i)
print(empty_list)

num = 0
while 1:
    print("真")
    num += 1
    if num > 10:
        break

for i in range(5):
    if i == 3:
        continue
    print(i)