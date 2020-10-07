
class Stack:

    def __init__(self):
        self.stack = []
        print('初始化完成')


    def append(self, value):
        self.stack.append(value)


    def pop(self):
        return self.stack.pop()


    def length(self):
        return len(self.stack)


    def getTop(self):
        if self.length() != 0:
            return self.stack[-1]
        return None


    def getStack(self):
        return self.stack


if __name__ == '__main__':
    s = Stack()
    for i in range(1, 5):
        s.append(i)
    print(s.getTop())
    print(s.pop())
    print(s.getStack())