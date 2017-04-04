from peewee import *

db = SqliteDatabase('congress.db')

class Rep(Model):
    firstName = CharField()
    lastName = CharField()
	state = CharField()
    national_rep = BooleanField()
	house = CharField()
	party = CharField()
	

    class Meta:
        database = db # This model uses the "people.db" database.
