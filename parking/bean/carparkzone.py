
#停车场区域，有的停车场分A区B区C区
#此车位剩余数量用于车场内引导用户停向有车位的区域

class CarParkZone():
    #停车场名，停车场车位数，usingSpaceNbr，地址，
    def __init__(self,id,carParkId,name,spaceNbr,usingSpaceNbr):
        self.id = id
        self.carParkId = carParkId
        self.name = name
        self.spaceNbr = spaceNbr
        self.usingSpaceNbr = usingSpaceNbr

    #新增停车区域
    def insertCarParkSpace(self,carParkSpace):
        return True

    #查询停车区域
    def selectCarParkSpace(self,id):
        return CarParkZone(id,id,'A区域','20','10')


