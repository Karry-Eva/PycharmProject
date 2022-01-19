from LinkedList import LinkedList
import pytest


# from LinkedNode import Node

class TestCase:
    def testAdd(self):
        linkedNode = LinkedList()
        assert linkedNode.isEmpty() is True
        linkedNode.isEmpty()

        linkedNode.add(1)
        linkedNode.add(2)
        linkedNode.add(3)
        linkedNode.append(4)
        linkedNode.append(5)  # 顺序：3-2-1-4-5
        list2 = linkedNode.priData()
        print(list2)
        assert list2 == [3, 2, 1, 4, 5]
        linkedNode.delNode(4)
        list3 = linkedNode.priData()
        print(linkedNode.search(0))
        assert list3 == [3, 2, 1, 5]
        assert linkedNode.search(0) is False
        linkedNode.insert(3, 4)
        list4 = linkedNode.priData()
        assert list4 == [3, 2, 1, 4, 5]
        assert linkedNode.length() == 5
        print(linkedNode.length())

if __name__ == '__main__':
    t = TestCase()
    t.testAdd()
