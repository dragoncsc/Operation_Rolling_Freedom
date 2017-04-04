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

	class Meta:
		order_by = ('firstName', )


def create_tables():
	db.connect()
	db.create_tables([Rep], True)
	db.close()

def add_rep( rep_list ):
	try:
		with db.transaction():
			rep = Rep.insert(
				firstName = rep_list[0],
				lastName = rep_list[1],
				state = rep_list[2],
				national_rep = rep_list[3],
				house = rep_list[4],
				party = rep_list[5]
			).execute()
			return rep
	except IntegrityError:
		print "something went horribly wrong"
			






