#!/usr/bin/env python
from abc import ABCMeta, abstractmethod

class Vehicle(object):
	__metaclass__ = ABCMeta

	@abstractmethod
	def __init__(self):
		pass

class Car(Vehicle):
	def __init__(self,regNo,color):
		self.regNo = regNo
		self.color = color
	def setRegno(regNo):
		self.regNo = regNo
	def getRegno():
		return self.regNo
	def setColor(color):
		self.color = color
	def getColor():
		return self.color
