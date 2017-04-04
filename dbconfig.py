from peewee import *

db = SqliteDatabase('congress.db')

class Rep(BaseModel):
    firstName = CharField()
    lastName = CharField()
	state = CharField()
    national_rep = BooleanField()
	house = CharField()
	party = CharField()

    class Meta:
		order_by = ('username', )
        database = db # This model uses the "people.db" database.



def create_tables():
	db.connect()
	db.create_tables([Rep], True)
	db.close()

def add_rep( rep_dict ):
	try:
		with db.transaction():
			rep = Rep.create(
				firstname = rep_dict['fname'],
				lastname = rep_dict['lname'],
				state = rep_dict['state'],
				national_rep = True,
				house = rep_dict['house'],
				party = rep_dict['party']
			)
	except IntegrityError:
		print "something went horribly wrong"
			






