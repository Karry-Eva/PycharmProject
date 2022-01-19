'''
定义单链表操作
'''

from LinkedNode import Node


class LinkedList:
    # 1、初始化链表为空
    def __init__(self):
        self._head = None
        # self._tail = None
        # self._length = 0

    # 2、检查是否为空
    def isEmpty(self):
        return self._head is None

    # 2-1、获取长度
    def length(self):
        curr = self._head
        count = 0
        while curr is not None:
            count += 1
            curr = curr.getNext()
        return count

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

    # 5、删除节点
    def delNode(self, value):
        curr = self._head
        pre = None
        while curr is not None:
            if curr.getValue() == value:
                if not pre:  # 删除头节点
                    self._head = curr.getNext()
                else:  # 删除中间节点
                    pre.setNext(curr.getNext())
                    break
            else:
                pre = curr
                curr = curr.getNext()

    # 6、查找
    def search(self, value):
        curr = self._head
        while curr is not None:
            if curr.getValue() == value:
                return True
            curr = curr.getNext()
        return False

    # 7、插入到某个固定位置
    def insert(self, index, value):
        if index <= 0:  # 头插
            self.add(value)
        elif index > (self.length() - 1):  # 尾插
            self.append(value)
        # 中间插
        else:
            curr = self._head
            count = 0
            newNode = Node(value)
            while count < index - 1:
                count += 1
                curr = curr.getNext()
            newNode.setNext(curr.getNext())
            curr.setNext(newNode)

    # 8、打印输出
    def priData(self):
        curr = self._head
        newList = []
        while curr is not None:
            newList.append(curr.getValue())
            curr = curr.getNext()
        return newList
