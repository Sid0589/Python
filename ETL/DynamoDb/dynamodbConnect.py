from boto.dynamodb2.table import Table
from boto import dynamodb2
import datetime
from datetime import datetime
import os 

class dynamodbConnect:

	def __init__(self):
		self.aws_region = None
		self.access_id  = None
		self.secret_key = None
		self.conn       = None

	def connect(self,aws_region,accessId,secretkey):
		try:
			self.aws_region = aws_region
			self.access_id  = accessId
			self.secret_key = secretkey
			self.conn=dynamodb2.connect_to_region(self.aws_region,aws_access_key_id =self.access_id,aws_secret_access_key=self.secret_key)
			return True
		except Exception as e:
			print 'Exception happened in dynamodb connect ' + str(e.args)
			exit(2)

	def putitem(self,tableName,items):
		if not self.conn:
			print "Connection is not created..exiting.."
			exit(2)
		try:
			self.conn.put_item(tableName,items)
			return True
		except Exception as e:
			print 'Exception happened in dynamodb putitem ' + str(e.args)
			exit(2)

	def deleteitem(self,tableName,delkey={}):
		if not self.conn:
			print "Connection is not created..exiting.."
			exit(2)
		if not delkey:
			print "Delete key is missing...exiting"
			exit(2)
		if not tableName:
			print "Table name is missing"
		try:
			self.conn.delete_item(table_name =tableName,key =delkey)
			return True
		except Exception as e:
			print 'Exception happened in dynamodb deleteitem method ' + str(e.args)
			exit(2)

	def updtablethroughput(self,tableName,throughput={'ReadCapacityUnits':5,'WriteCapacityUnits':5}):
		if not self.conn:
			print "Connection is not created..exiting.."
			exit(2)
		try:	
			self.conn.update_table(table_name=tableName,provisioned_throughput=throughput)
			return True
		except Exception as e:
			print 'Exception happened in dynamodb updatetable method ' + str(e.args)
			exit(2)

	def gettablethroughput(self,tableName):
		if not self.conn:
			print "Connection is not created ...exiting"
			exit(2)
		try:
			tableInfo = self.conn.describe_table(tableName)
			result    = {'ReadCapacityUnits':tableInfo['Table']['ProvisionedThroughput']['ReadCapacityUnits'],
			             'WriteCapacityUnits':tableInfo['Table']['ProvisionedThroughput']['WriteCapacityUnits']
			            }
			return result
		except Exception as e:
			print 'Exception happened in gettablethroughput dynamodb method ' + str(e.args)
			exit(2)
