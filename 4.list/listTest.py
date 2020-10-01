"""
列表
split
序号切片
pop
append
len
remove
"""
listTest = [1, 2, 3, 4, 5]
strTest = '1 2 3 4 5'
print(strTest.split(' '))
listTest.append('jesse')
print(listTest)
print(listTest.pop())
print(listTest)
print(listTest.remove(3))

print(listTest[0])
print(listTest[1])
print(listTest[1:3])

print(len(listTest))