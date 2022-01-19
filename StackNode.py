import pytest

class Stack1:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, value):
        self.items.append(value)

    def pop(self):
        self.items.pop()

    def peek(self):
        if self.items is not None:
            return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    # 类没有定义__str__或__repr__方法，因此print使用默认表示。如果要将Stack的实例打印为列表
    '''
    如果要把一个类的实例变成 str，就需要实现特殊方法__str__()：
    不使用 __str__  ，print打印出来是个对象；使用了就把对象变成字符串
    '''
    def __str__(self):
        # print(type(self.items))
        return str(self.items)


if __name__ == '__main__':
    s = Stack1()
    s.push('i love life')
    print(s.peek())
    s.push('word')
    s.push('hello')
    s.push(8.9)
    print(s)
    # assert s.pop() == 8.9
    s.pop()
    print(s)
    # assert s.pop() == 'hello'
    s.pop()
    print(s)
