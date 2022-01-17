# python   基本数据结构#
'''
一、数组与链表：
    - 数组：list、tuple、dict
    - 单 / 双向链表
二、栈与队列【重点！！！】
    - 栈
    - 队列
三、哈希表
四、堆：最大堆 ／ 最小堆
五、树与图：最近公共祖先、并查集
六、字符串：前缀树（字典树） ／ 后缀树
'''


#  定义一个单节点node类
class Node:
    def __init__(self, value=None, next=None):
        self._value = value
        self._next = next

    def getValue(self):
        return self._value

    def getNext(self):
        return self._next

    def setValue(self, new_value):
        self._value = new_value

    def setNext(self, new_next):
        self._next = new_next

