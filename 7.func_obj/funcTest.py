"""
面向过程 函数
参数传递
返回

面向对象 类
栈的数据结构实现
"""

def add(a, b):
    return a + b


def main():
    # 强转数字
    a, b = input('>>>').split(' ')
    print('a is %d, b is %d' % (int(a), int(b)))
    return add(int(a), int(b))


if __name__ == '__main__':
    result = main()
    print(result)