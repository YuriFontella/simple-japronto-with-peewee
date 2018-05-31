import peewee, psycopg2
from db.connect import DBpgsql

db = DBpgsql()

class Users(peewee.Model):
    name = peewee.CharField()
    email = peewee.CharField()
    password = peewee.CharField()

    class Meta:
        database = db.connect()
