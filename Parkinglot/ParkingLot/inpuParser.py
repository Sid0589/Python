#!/usr/bin/env python
from ParkingLot import ParkingLot
import sys
import os

class inputParser(object):
    @classmethod
    def inputParse(cls, args):
        inputString = None
        inputs = []
        exit_app = False
        parkinglot = ParkingLot()
        try:
            if len(args) > 0:
                inputFileName = args[0]
                if os.path.exists(inputFileName):
                    inputfile = open(inputFileName,'r')
                else:
                    print "File did not find..check the path\n"
                    exit(2)
            while not exit_app:
                if len(args) == 0:
                    inputString = raw_input("Enter Command :")
                else:
                    try:
                        inputString = inputfile.next().replace('\n','')
                    except StopIteration:
                        inputString = "exit"
                if inputString.strip()!='':
                    inputs = inputString.split(' ')
                else:
                    continue
                if  len(inputs)!=0: 
                    if inputs[0]=="create_parking_lot":
                        if not parkinglot.isParkingLotCreated():
                            if len(inputs) == 2:
                                try:
                                    parkinglot.createParkingLot(inputs[1])
                                except Exception as e:
                                    print "Inavlid input passed.\n"
                                    print str(e.args)
                                    print "maximum Input accepted is : 2147483647.\n"
                            else:
                                print "Invalid input passed.\n"
                        else:
                            print "Parking lot already created.\n"
                    elif inputs[0]=="park":
                        if parkinglot.isParkingLotCreated():
                            if len(inputs) == 3:
                                parkinglot.park(inputs[1], inputs[2])
                            else:
                                print "Invalid input passed.\n"
                        else:
                            print "Parking lot is Not Created.\n"
                    elif inputs[0]=="leave":
                        if parkinglot.isParkingLotCreated():
                            if len(inputs)  == 2:
                                try:
                                    parkinglot.leave(inputs[1])
                                except Exception as e:
                                    print "Inavlid input passed.\n"
                                    print str(e.args)
                                    print "maximum Input accepted is :\n"
                            else:
                                print "Invalid input passed.\n"
                        else:
                            print "Parking lot is Not Created.\n"
                    elif inputs[0]=="status":
                        if parkinglot.isParkingLotCreated():
                            if len(inputs) == 1:
                                parkinglot.status()
                            else:
                                print "Invalid input passed.\n"
                        else:
                            print "Parking lot is Not Created.\n"
                    elif inputs[0]=="registration_numbers_for_cars_with_colour":
                        if parkinglot.isParkingLotCreated():
                            if len(inputs) == 2:
                                parkinglot.getRegistrationNumbersFromColor(inputs[1])
                            else:
                                print "Invalid input passed.\n"
                        else:
                            print "Parking lot is Not Created.\n"
                    elif inputs[0]=="slot_numbers_for_cars_with_colour":
                        if parkinglot.isParkingLotCreated():
                            if len(inputs) == 2:
                                parkinglot.getSlotNumbersFromColor(inputs[1])
                            else:
                                print "Invalid input passed.\n"
                        else:
                            print "Parking lot is Not Created.\n"
                    elif inputs[0]=="slot_number_for_registration_number":
                        if parkinglot.isParkingLotCreated():
                            if len(inputs) == 2:
                                parkinglot.getSlotNumberFromRegNo(inputs[1])
                            else:
                                print "Invalid input passed.\n"
                        else:
                            print "Parking lot is Not Created.\n"
                    elif inputs[0]=="exit":
                        if parkinglot.isParkingLotCreated():
                            parkinglot.deleteParkingLot()
                            del parkinglot
                        exit_app = True
                    else:
                        print "Invalid command Entered.\n"
        except Exception as e:
            print str(e.args)
            print "App Terminated"
            exit(2)