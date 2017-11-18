#!/usr/bin/env python
import sys
import unittest
import os
from StringIO import StringIO
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from ParkingLot import ParkingLot,inputParser


class test_parkinglot(unittest.TestCase):
    def test_createParkingLot(self):
    	parkingLot = ParkingLot.ParkingLot()
    	result = StringIO()
    	sys.stdout = result
        parkingLot.createParkingLot('2')
        res = result.getvalue()
        self.assertEqual(2, parkingLot.MAX_SIZE)
        self.assertEqual(2, len(parkingLot.availableSlotList))
        self.assertEqual(res.replace('\n',''),'Created parking lot with 2 slots')
        del parkingLot

    def test_park(self):
        parkingLot = ParkingLot.ParkingLot()
        result = StringIO()
        sys.stdout = result
        parkingLot.park("KA-01-HH-1234", "White")
        parkingLot.createParkingLot('1')
        parkingLot.park("KA-01-HH-1234", "White")
        parkingLot.park("KA-01-HH-9999", "White")
        res = result.getvalue()
        self.assertEqual(res.replace('\n',''),"Sorry, parking lot is not createdCreated parking lot with 1 slotsAllocated slot number: 1Sorry, parking lot is full")
        self.assertEqual(0, len(parkingLot.availableSlotList))
        del parkingLot

    def test_leave(self):
    	parkingLot = ParkingLot.ParkingLot()
        result = StringIO()
        sys.stdout = result
        parkingLot.leave('2')
        parkingLot.createParkingLot('1')
        parkingLot.park("KA-01-HH-1234", "White")
        parkingLot.leave('1')
        res = result.getvalue()
        self.assertEqual(res.replace('\n',''),"Sorry, parking lot is not createdCreated parking lot with 1 slotsAllocated slot number: 1Slot number 1 is free")
        del parkingLot

    def test_status(self):
    	parkingLot = ParkingLot.ParkingLot()
        result = StringIO()
        sys.stdout = result
        parkingLot.status()
        parkingLot.createParkingLot('1')
        parkingLot.park("KA-01-HH-1234", "White")
        parkingLot.status()
        res = result.getvalue()
        self.assertEqual(res.replace('\n',''),"Sorry, parking lot is not createdCreated parking lot with 1 slotsAllocated slot number: 1Slot No.\tRegistration No.\tColour1\tKA-01-HH-1234\tWhite")
        del parkingLot

    def test_getRegistrationNumbersFromColor(self):
    	parkingLot = ParkingLot.ParkingLot()
        result = StringIO()
        sys.stdout = result
        parkingLot.getRegistrationNumbersFromColor("White")
        parkingLot.createParkingLot('1')
        parkingLot.park("KA-01-HH-1234", "White")
        parkingLot.getRegistrationNumbersFromColor("White")
        res = result.getvalue()
        self.assertEqual(res.replace('\n',''),"Sorry, parking lot is not createdCreated parking lot with 1 slotsAllocated slot number: 1KA-01-HH-1234")
        del parkingLot

    def test_getSlotNumbersFromColor(self):
    	parkingLot = ParkingLot.ParkingLot()
        result = StringIO()
        sys.stdout = result
        parkingLot.getSlotNumbersFromColor("White")
        parkingLot.createParkingLot('1')
        parkingLot.park("KA-01-HH-1234", "White")
        parkingLot.getSlotNumbersFromColor("White")
        res = result.getvalue()
        self.assertEqual(res.replace('\n',''),"Sorry, parking lot is not createdCreated parking lot with 1 slotsAllocated slot number: 11")
        del parkingLot

    def test_getSlotNumberFromRegNo(self):
    	parkingLot = ParkingLot.ParkingLot()
    	result = StringIO()
        sys.stdout = result
        parkingLot.getSlotNumberFromRegNo("KA-01-HH-1234")
        parkingLot.createParkingLot('1')
        parkingLot.park("KA-01-HH-1234", "White")
        parkingLot.getSlotNumberFromRegNo("KA-01-HH-1234")
        res = result.getvalue()
        self.assertEqual(res.replace('\n',''),"Sorry, parking lot is not createdCreated parking lot with 1 slotsAllocated slot number: 11")
        del parkingLot


if __name__ == '__main__':
	unittest.main()