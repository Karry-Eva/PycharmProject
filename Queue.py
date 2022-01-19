'''
队列：方法1-借助list列表实现
1、isEmpty()
2、dequeue
3、enqueue(item)
4、size()
5、Queue()
'''


class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.size() == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)


if __name__ == '__main__':
    queue = Queue()
    print(queue.isEmpty())
    queue.enqueue("i like reading")
    queue.enqueue("hello")
    queue.enqueue([1, 'test', 'run'])
    print(queue)
    queue.dequeue()
    print(queue)
    print(queue.size())
