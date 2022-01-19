import time

import pytest
import json

# class Test_exec1:
#     if __name__ == '__main__':
#         print(" ")

iplist = ["172.20.116.70", "172.20.116.72"]
ips = ','.join(iplist)

data_file = open('data.json', 'r', encoding='utf-8')
a = json.load(data_file)


# print(a)

# 批量测试装饰器，类似于for ip in iplist
# @pytest.mark.parametrize('ip', iplist)
# def test_cpu(ip):
#     value = a['data']['CPU'][ip]['cpu_prct_used'][0]
#     assert float(value.strip("%")) < 80
#
#
# # pytest内置函数fixture
# # 方法1：入门实例
# # before函数被定义为Fixture，其他函数要调用这个Fixture，把它当成一个参数即可
# # test_1和test_2运行之前都调用了before，也就是before执行了两次。
# # 默认情况下，fixture是每个测试用例如果调用了该fixture就会执行一次的。
# @pytest.fixture()
# def before():
#     print('\nbefore each test')
#
#
# def test_1(before):
#     print('test_1()')
#
#
# def test_2(before):
#     print('test_2()')
#     assert 0
#
#
# # 方法2：调用fixture是带参数的，params
# # 对于param里面的每个值，fixture都会去调用执行一次，
# # 就像执行for循环一样把params里的值遍历一次。
# @pytest.fixture(params=[1, 2, 3])
# def test_data(request):
#     return request.param
#
#
# def test_not_2(test_data):
#     print('test_data: %s' % test_data)
#     assert test_data != 2


# 方法3：使用autos调用fixture
# fixture decorator一个optional的参数是autouse, 默认设置为False。
# 当默认为False，就可以选择用上面两种方式来试用fixture。
# 当设置为True时，在一个session内的所有的test都会自动调用这个fixture。

# fixture scope
# function：每个test都运行，默认是function的scope
# class：每个class的所有test只运行一次
# module：每个module的所有test只运行一次
# session：每个session只运行一次

@pytest.fixture(scope="module", autouse=True)
def mod_header(request):
    print("\n----------------------")
    print("module : %s" % request.module.__name__)
    print('------------------------')


@pytest.fixture(scope="function", autouse=True)
def func_header(request):
    print('\n----------------------')
    print('function : %s' % request.function.__name__)
    print('time : %s' % time.asctime())
    print('------------------------')


def test_one():
    print('in test_one()')


def test_two():
    print('in test_two()')
