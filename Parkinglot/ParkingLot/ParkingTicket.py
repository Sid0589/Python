class ParkingTicket(object):
    parkedCar = Car()
    def __init__(self, carToPark, slotNumber):
        self.parkedCar = carToPark
        self.slotNumber = slotNumber
    def getParkedCar(self):
        return self.parkedCar
    def getSlotNumber(self):
        return self.slotNumber
