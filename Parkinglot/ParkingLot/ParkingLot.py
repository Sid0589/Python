#!/usr/bin/env python
class ParkingLot(object):
    MAX_SIZE = 0
    class Car(object):
        regNo = None
        color = None
        def __init__(self, regNo, color):
            self.regNo = regNo
            self.color = color
    
    def __init__(self):
        self.availableSlotList =[]        #  Available slots list
        self.SlotCarMap ={}               #  Map of Slot, Car
        self.RegNoSlotMap ={}             #  Map of RegNo, Slot
        self.ColorRegNoMap ={}            #  Map of Color, List of RegNo

    def createParkingLot(self, lotCount):
        if lotCount.isdigit():
            try:
                self.MAX_SIZE = int(lotCount)
            except Exception as e:
                print "Invalid lot count"
            self.availableSlotList = []
            i = 1
            while i <= self.MAX_SIZE:
                self.availableSlotList.append(i)
                i += 1
            print "Created parking lot with " + str(lotCount) + " slots"
        else:
            print "Please provide integer input"
            exit(2)

    def isParkingLotCreated(self):
        if self.MAX_SIZE ==0:
            return False
        else:
            return True

    def deleteParkingLot(self):
        self.availableSlotList =[]  #  Available slots list
        self.SlotCarMap ={}               #  Map of Slot, Car
        self.RegNoSlotMap ={}               #  Map of RegNo, Slot
        self.ColorRegNoMap ={}

    def park(self, regNo, color):
        if self.MAX_SIZE == 0:
            print "Sorry, parking lot is not created"
        elif len(self.SlotCarMap) == self.MAX_SIZE:
            print "Sorry, parking lot is full"
        else:
            self.availableSlotList.sort()
            slot = self.availableSlotList[0]
            self.SlotCarMap[slot]  = ParkingLot.Car(regNo,color)
            self.RegNoSlotMap[regNo] = slot
            if color in self.ColorRegNoMap.keys():
                self.ColorRegNoMap[color].append(regNo)
            else:
                regNoList =[]
                regNoList.append(regNo)
                self.ColorRegNoMap[color] =regNoList 
            print "Allocated slot number: " + str(slot)
            self.availableSlotList = self.availableSlotList[1:]

    def leave(self, slotNo):
        if slotNo.isdigit():
            slotNo = int(slotNo)
            if self.MAX_SIZE == 0:
                print "Sorry, parking lot is not created"
            elif len(self.SlotCarMap) > 0:
                carToLeave = self.SlotCarMap[slotNo]
                if carToLeave != None:
                    self.SlotCarMap.pop(slotNo,None)
                    self.RegNoSlotMap.pop(carToLeave.regNo)
                    if carToLeave.regNo in self.ColorRegNoMap[carToLeave.color]:
                        self.ColorRegNoMap[carToLeave.color].remove(carToLeave.regNo)
                    self.availableSlotList.append(slotNo)
                    print "Slot number " + str(slotNo) + " is free"
                else:
                    print "Slot number " + str(slotNo) + " is already empty" 
            else:
                print "Parking lot is empty"
        else:
            print "Please provide integer input"
            exit(2)

    def status(self):
        if self.MAX_SIZE == 0:
            print "Sorry, parking lot is not created"
        elif len(self.SlotCarMap) > 0:
            print "Slot No.\tRegistration No.\tColour"
            i=1
            while i <= self.MAX_SIZE:
                if i in self.SlotCarMap.keys():
                    car = self.SlotCarMap[i]
                    print str(i) + "\t" + car.regNo + "\t" + car.color
                i += 1 
        else:
            print "Parking lot is empty"

    def getRegistrationNumbersFromColor(self, color):
        if self.MAX_SIZE == 0:
            print "Sorry, parking lot is not created"
        elif color in self.ColorRegNoMap.keys():
            regNoList = self.ColorRegNoMap[color]
            i =0
            while i < len(regNoList):
                if not (i == len(regNoList) - 1):
                    print regNoList[i] + ","
                else:
                    print regNoList[i]
                i += 1
        else:
            print "Not found"

    def getSlotNumbersFromColor(self, color):
        if self.MAX_SIZE == 0:
            print "Sorry, parking lot is not created"
        elif color in self.ColorRegNoMap.keys():
            regNoList = self.ColorRegNoMap[color]
            i =0
            j =0
            slotList =[]
            while i < len(regNoList):
                slotList.append(self.RegNoSlotMap[regNoList[i]])
                i += 1
            slotList.sort()
            while j < len(slotList):
                if not (j == len(slotList) - 1):
                    print str(slotList[j]) + ","
                else:
                    print str(slotList[j])
                j += 1
        else:
            print "Not found"

    def getSlotNumberFromRegNo(self, regNo):
        if self.MAX_SIZE == 0:
            print "Sorry, parking lot is not created"
        elif regNo in self.RegNoSlotMap.keys() :
            print self.RegNoSlotMap[regNo]
        else:
            print "Not found"
