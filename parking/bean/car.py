
#车
class Car():
    def __init__(self,id,name,licenseplate):
        self.id = id
        self.name = name
        #车牌
        self.licenseplate = licenseplate
    
    #新增car入库
    def insertCar(self,car):
        return True

    #查询car
    def selectCar(self,licenseplate):
        return Car('2','汉兰达',licenseplate) 

    #更新车辆信息
    def updateCar(self,car):
        return True


