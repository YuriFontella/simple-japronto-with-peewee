from playhouse.postgres_ext import PostgresqlExtDatabase

class Database:

  conn = None

  def __init__(self):
    self.connect()


  def connect(self):
    if self.conn is None:
      self.conn = PostgresqlExtDatabase('db_dev', user='postgres', password='123456', host='127.0.0.1', port='5432')


    return self.conn
