# def div(a,b):
#     try:
#         return a/b
#     except:
#         return
# print(div(11,0))

# def f(a,b):
# #     try:
# #         print(a/b)
# #     except ZeroDivisionError as e:
# #         print(e)
# #     else:
# #         print("成功执行")
# #     finally:
# #         print("失败执行")git commit -m
# # print(f(6,5))

class CustomException(Exception):
    def __init__(self,value = "值不能为0"):
        self.value = value
    def __str__(self):
        return  self.value
a = 0
try:
    if a==0:
        print("a={}触发异常".format(a))
        raise CustomException
    print("a={}未触发异常".format(a))
except CustomException as e:
    print(e)