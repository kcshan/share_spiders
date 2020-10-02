'''
字典

增加
查找
删除
改变
取出所有
'''

# 键值对
dictTest = {
    'one': 'zygx8',
    'two': 'jesse'
}
print(dictTest)

# 增加
dictTest['three'] = 'zygx8'
print(dictTest)

# 删除
del dictTest['one']
print(dictTest)
print(dictTest.pop('two'))

# 改变
dictTest['three'] = 'jesse'
print(dictTest)

# 查找
print(dictTest['three'])
print(dictTest.get('three'))

# 取出所有
print(dictTest.items())

