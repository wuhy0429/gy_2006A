# from day03 import module_1
# print(module_1.a)
# module_1.name()
# print(module_1.test.name)

# from day03.module_1 import a as module_1_a,name as module_1_name,test as module_1_test
# print(module_1_a)
# module_1_name()
# print(module_1_test.name)

a = "我是模块2的a变量"
def name():
    print("我是模块2的name方法")
class test():
    name = "我是模块2的test类"

if __name__ == '__main__':   #闷方法
    name()
    print(test.name)