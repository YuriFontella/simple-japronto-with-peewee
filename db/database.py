from peewee import PostgresqlDatabase

class Database:

  conn = None

  def __init__(self):
    self.connect()


  def connect(self):
    if self.conn is None:
      self.conn = PostgresqlDatabase('db_dev', user='postgres')


    return self.conn
