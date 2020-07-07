# y = ["果芽","老干妈","腾讯","阿里","百度"]
# if ("果芽" in y):
#     print("合作方")
# else :
#     print("非合作方")
#
#
# c = 66.5
# if (c > 0 and c < 59):
#     print("不及格")
# elif (c >= 60 and c <= 70):
#     print("及格")
# elif (c >= 71 and c <= 80):
#     print("良好")
# elif (c >= 81 and c <= 100):
#     print("优秀")
# else:
#     print("请输入正确的成绩")
#
#
# c_1 = [20,35,45,55,68,99,88,77,]
# for c in c_1:
#     if (c > 0 and c < 59):
#         print("不及格")
#     elif (c >= 60 and c <= 70):
#         print("及格")
#     elif (c >= 71 and c <= 80):
#         print("良好")
#     # elif (c >= 81 and c <= 100):
#         print("优秀")
#     else:
#         print("请输入正确的成绩")
# s = 1
# for i in range(10,0,-1):
#     s *= i
# print(s)
#
# flag = True
# a = 66
# while flag:
#     b = int(input("请输入数字"))
#     if(b > a):
#         print("大了")
#     elif(b < a):
#         print("小了")
#     else:
#         print("猜对了")
#         flag = False
#
# while True:
#     b = int(input("请输入数字"))
#     if(b > a):
#         print("大了")
#     elif(b < a):
#         print("小了")
#     else:
#         print("猜对了")
#         break

# for i in range(1,100,1):
#     if i % 3 !=0:
#         continue
#     print(i)

# 定义一个求两个数商和余数的方法
# a = 60
# b = 19
# print("商:",a // b,"余数:",a % b,)

# def nmber(a,b):
#     if(b == 0):
#         print("除数不能为0")
#     else:
#         print("商:", a // b, "余数:", a % b, )
# nmber(8,0)
# def shang_yu(a,b):
#     if(b == 0):
#         return None
#     else:
#         return (a//b,a%b)
# # haha = shang_yu(2,20)  #按照位置传参
# haha = shang_yu(b=2,a=20) #按照关键字传参，可无序写入
# if haha is None:
#     print("参数错误")
# else:
#     print("商为：",haha[0],"余数为：",haha[1])
#
# def sm(a,b=2):# 设置默认值参数
#     return a+b
# print(sm(2))
# print(sm(2,b=4))

#
# def sum1(*arge): #*arge接受动态位置参数，**kwargs接受动态关键字位置
#     s = 0
#     for i in arge:
#         s +=i
#     return  s
# print(sum1(1,2))

# def sum1(name,**kwargs):
#     print(name)
#     print(kwargs)
#     for i in kwargs:
#         return kwargs
# print(sum1(name="哈哈",name1="嘻嘻嘻"))

# 面向对象
# class calc():   #类名
#     a=None
#     b=None
#     c=None
#     def input(self,a,b):
#         self.a=a
#         self.b=b
#     def sum(self):
#         self.res = self.a + self .b
#     def div(self):
#         self.res = self.a /self.b
#     def get_result(self):
#         print(self.res)
#
# c = calc() #类的实例化 c就是对象
#
# c.input(10,20)
# c.sum()
# c.get_result()
# c.div()
# c.get_result()
#
# c.input(30,20)
# c.sum()
# c.get_result()
# c.div()
# c.get_result()


# class calc():   #魔法函数，类的实例化的时候调用，又称构造方法
#     c=None
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def input(self,a,b):
#         self.a=a
#         self.b=b
#     def sum(self):
#         self.res = self.a + self .b
#     def div(self):
#         self.res = self.a /self.b
#     def get_result(self):
#         print(self.res)
#
# c = calc(20,96)
# c.sum()
# c.get_result()
# c.div()
# c.get_result()

# # 九九乘法表
# for a in range(1,10):
#     for b in range(1,a+1):
#        print(b,"x",a,"=",a*b,end="\t")
#     print()

# 冒泡排序
w = [5,4,15]

print(w[0+1])
length = len(w)
print(w[length-1])# length = len() 内置函数，表示查询列表内有多少数
for i in range(length-1,0,-1):   # 外层循环确定排好序的数据下表
    for j in range(i):           # 遍历未排好序的列表
        if(w[j] > w[j+1]):       # 判断相邻两个数据，前边的如果大于后边的，则交换两个数据的位置
            w[j],w[j+1] = w[j+1],w[j]
print(w)
