#停车记录
import datetime

class ParkingRecord():
    #停车场id，停车场车位数，usingSpaceNbr，地址，
    def __init__(self,id,carParkId,carParkZoneId,carParkSpaceId,carId,licenseplate,starttime):
        self.id = id
        self.carParkId = carParkId
        self.carParkZoneId = carParkZoneId
        self.carParkSpaceId = carParkSpaceId
        self.carId = carId
        self.licenseplate = licenseplate
        self.starttime = starttime
        self.endtime = None


