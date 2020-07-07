# a = 857
# b = "857"
# print(a + int(b))   # 字符串转数字 ，字符串内必须为数字
# print(str(a) + b)
# print(list(b))
# # 列表，元组，集合 之可以互转
# c = [8,5,7]
# d = (8,5,7)
# e = {8,5,7}
# print(tuple(c)
# print(set(d))
# print(list(e))

# 打开模式：r 读取 ，w 清空写入， a 追加写入， b 二进制模式
# a = open ("haha.txt","w")   # open 打开文件
# a.write("哈哈哈""\n""xixixi""\n")   # write 写入内容至打开的文件
# a.close()                     #关闭文件
# 换行输入
# b ='''jhgfjhfg
# # jvkjkgd
# # hfjgfh'''
# # a = open ("haha.txt","w")
# # a.write(b)
# # a.close()

# a = open("haha.txt","r")
# print(a.read())  #默认读取全部内容
# print(a.read(10))#读取内容的大小
# print(a.readline())#按行读取，读取一行
# print(a.readlines())#按行读取，读取所有行

# for i in range(1,10):
#     for j in range(1,i+1):
#         print("%d x %d = %d"%(j,i,j*i),end="\t")
#     print()
# for i in range (1,10):
#     for j in range (1,i+1):
#         print("{} x {} ={}".format(j,i,j*i),end="\t")
#     print()


# l = [5,9,6,4,8,52]
# l[0] = 16
# print(l)
# l[2:5] =8,5,7
# print(l)
# l[1:-2:2] = 857,857
# print(l)

# #新增数据
# l = [8,5,7]
# l.append("哈哈")     #插入一条内容，显示再最后
# l.extend({"name",857}) #插入多条内容，显示在最后
# l.insert(1,"嘻嘻")     # 选择下标位置后插入内容
# print(l)
# #删除
# print(l.pop(2))   #根据下标删除
# print(l)
# l.remove("name") #根据数据内容删除，出现同名删除第一个
# print(l)
# # 在pychar里ture代表1，false代表0，推荐用下标删除


# d ={"name":"大郎","age":"857"}
# d["age"] = "857857"    # 一样的key 则数据内容会覆盖
# print(d)
# d.update({"addr":"宋","aihao":"喝药"})  # 不一样的key 则直接写入
# print(d)