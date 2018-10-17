
#用户
class User():
    def __init__(self,id,name,phoneNbr,age):
        self.id = id
        self.name = name
        self.phoneNbr = phoneNbr
        self.age = age

        #新增car入库
    def insertUser(self,user):
        return True

    #查询car
    def selectUser(self,phoneNbr):
        return User(2,'张三',phoneNbr,40) 

    #更新车辆信息
    def updateUser(self,user):
        return True

