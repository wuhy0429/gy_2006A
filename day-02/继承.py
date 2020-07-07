# class Father():
# #     money = 100000000
# #     house = 1000
# #     __nei_ku = 10
# #     def shou_yi(self):
# #         print("渣男成长记")
# #
# #
# # class Erzi(Father):
# #     ai_hao = "买买买"
# #     pass
# #
# # e = Erzi()
# # print(e.ai_hao)
# # print(e.house)
# # print(e.money)
# # e.shou_yi()



class Father():
    money = 100000000
    house = 1000
    __nei_ku = 10

    def __init__(self,haha):
        self.haha = haha

    def shou_yi(self):
        print("渣男成长记")


class Erzi(Father):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)  #父承子集  调用实例 用super
    ai_hao = "买买买"
    pass
e = Erzi(88621)
print(e.ai_hao)
print(e.house)
print(e.money)
e.shou_yi()