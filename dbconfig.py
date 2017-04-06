'''
Shell of dbconfig file, currently only db model for reps have been defined
TODO: 
1) add more relevant fields for Rep, 
2) create Bill Model
3) create relationship mapping between Rep and Bill

'''

from peewee import *

db = SqliteDatabase('congress.db')

class BaseModel(Model):
	class Meta:
		database = db

class Rep( BaseModel ):
	firstName = CharField()
	lastName = CharField()
	state = CharField()
	national_rep = BooleanField()
	house = CharField()
	party = CharField()
	rep_id = CharField()
	url = CharField()

	class Meta:
		order_by = ('firstName', )

class Bill( BaseModel ):
	number = CharField()
	title = CharField()
	committee = CharField()
	introduced = CharField()
	bill_uri = CharField()
	class Meta:
		order_by = ('number', )

def create_tables():
	db.connect()
	db.create_tables([Rep, Bill], True)
	db.close()

def add_bill( bill_list ):
	try:
		with db.transaction():
			bill = Bill.insert(
				number = bill_list[0],
				title = bill_list[1],
				committee = bill_list[2],
				introduced = bill_list[3],
				bill_uri = bill_list[4]
			).execute()
			return bill
	except IntegrityError:
		print "Bill ", bill_list[1], " couldn't be stored"
		print "It may already be in the system"


def add_rep( rep_list ):
	try:
		with db.transaction():
			rep = Rep.insert(
				firstName = rep_list[0],
				lastName = rep_list[1],
				state = rep_list[2],
				national_rep = rep_list[3],
				house = rep_list[4],
				party = rep_list[5],
				rep_id = rep_list[6],
				url = rep_list[7]
			).execute()
			return rep
	except IntegrityError:
		print "Representative ", rep_list[0], " couldn't be stored"
		print "He/she may already be in the system"
			








