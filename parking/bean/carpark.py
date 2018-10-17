
#停车场
class CarPark():
    #停车场名，停车场车位数，已使用车位数，场内当前车辆数量，地址，
    def __init__(self,id,name,spaceNbr,usingSpaceNbr,insideCarNbr,address):
        self.id = id
        self.name = name
        self.spaceNbr = spaceNbr
        self.usingSpaceNbr = usingSpaceNbr
        self.insideCarNbr = insideCarNbr
        self.address = address

    #新增停车场
    def insertCarPark(self,carPark):
        return True

    #查询停车场
    def selectCarPark(self,id):
        return CarPark(id,'昂立软件园停车场','50','40','41','辽宁省沈阳市浑南区高歌路2号')

    def updateCarPark(self,carPark):
        return True


