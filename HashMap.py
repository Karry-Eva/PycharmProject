"""
散列表：
- 开放寻址法：https://zhuanlan.zhihu.com/p/63527627
- 链表法：https://www.cnblogs.com/linxiyue/p/3795396.html

- HashTable(size) # 类初始化
- hash(key) # 定义hash函数
- insert_hash(key, value) # 插入
- search_hash(key) # 查找
"""


class HashTable:
    def __init__(self, size):
        self.items = [None for i in range(size)]
        self.count = size  # 最大表长

    def hash(self, key1):
        index = key1 % self.count
        return index

    # 若无hash冲突，则直接添加
    # hash冲突时，则根据开放寻址法，查找新的不冲突的地址
    def insert_hash(self, key1, value):
        index = self.hash(key1)
        # print(index)
        while self.items[index]:
            index = (index + 1) % self.count
        self.items[index] = value

    def search_hash(self, key):
        star = index = hash(key)
        while self.items[index] != key:
            index = (index + 1) % self.count
            if not self.items[index] or index == star:  # 说明没找到或者循环到了开始的位置
                return False
        return True

    def __str__(self):
        return str(self.items)


if __name__ == '__main__':
    hashTable = HashTable(5)
    list1 = [(11, "i love u"), (20, "hello"), (31, 0), (43, "test")]
    for key, value in list1:
        print(key, value)
        hashTable.insert_hash(key, value)
        print(hashTable)
    print(hashTable)
