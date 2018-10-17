
#车位
class CarParkSpace():
    def __init__(self,id,carParkId,carParkZoneId,price,isusing):
        self.id = id
        self.carParkId = carParkId
        self.carParkZoneId = carParkZoneId
        self.price = price
        self.isusing = isusing

    #新增车位
    def insertCarParkSpace(self,carParkSpace):
        return True

    #查询车位
    def selectCarParkSpace(self,id):
        return CarParkSpace(id,id,id,'5','未使用')

    #更新车位
    def updateCarParkSpace(self,carParkSpace):
        return True