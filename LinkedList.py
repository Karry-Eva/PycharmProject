'''
定义单链表操作
'''

from LinkedNode import Node
class LinkedList:
    # 1、初始化链表为空
    def __init__(self):
        self._head = None
        self._tail = None
        self._length = 0

    # 2、检查是否为空
    def isEmpty(self):
        return self._head == None

    # 3、链表前端添加元素
    def add(self, value):
        newNode = Node(value)
        newNode.setNext(self._head)
        self._head = newNode

    # 4、链表尾部添加元素
    def append(self, value):
        newNode = Node(value)
        if self.isEmpty():
            self._head = newNode
        else:
            current = self._head
            while current.getNext() is not None:
                current = current.getNext()
            current.setNext(newNode)
