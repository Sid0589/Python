import csv
import datetime
import psycopg2
from datetime import datetime
import os 

class redshiftConnect:
	def __init__(self):
		self.host = None
		self.port = None
		self.database = None
		self.authuser = None
		self.password = None
		self.conn     = None

	def connect(self,**connconfig):
		configparamL = ['host','port','database','authuser','password']
		for eachcparam in configparamL:
			if eachcparam not in connconfig.keys():
				print "%s key is missing in connection dictionary" %(eachcparam)
				exit(2)
		self.host = connconfig['host']
		self.port = connconfig['port']
		self.database = connconfig['database']
		self.authuser = connconfig['authuser']
		self.password = connconfig['password']
		try:
			self.conn = psycopg2.connect('''dbname='%s' user='%s' host='%s' port=%d password='%s' ''' %(self.database,self.authuser,self.host,self.port,self.password))
			return True
		except Exception as e:
			print 'Exception happened in rs connect method' + str(e.args)
			exit(2)

	def getResultSet(self,sqlQuery,fileName):
		if not self.conn:
			print "No connection object found...exiting"
			exit(2)
		try:
			crsr = self.conn.cursor()
			crsr.execute(sqlQuery)
			fetchRs = crsr.fetchmany(10000)
			fileObj = open(fileName,'w')
			header  = ''.join(i[0] for i in crsr.description)
			fileObj.write(header + '\n')
			while fetchRs:
				for i in fetchRs:
					fileObj.write(''.join(['' if x is None else str(x).replace('\n','~').replace('\r','~').replace('',' ').replace('\0','') for x in i ]) + '\n')
				fetchRs = crsr.fetchmany(10000)
			fileObj.close()
			crsr.close()
			self.conn.close()
			return True
		except Exception as e:
			print 'Exception happened in getResultSet method ' + str(e.args)
			return False
