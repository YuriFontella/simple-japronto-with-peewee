import peewee
from db.database import Database

db = Database()

class Users(peewee.Model):
    name = peewee.CharField()
    email = peewee.CharField()
    password = peewee.CharField()

    class Meta:
        database = db.connect()
