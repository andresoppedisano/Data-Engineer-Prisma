import sqlalchemy as db

import sqlalchemy
import sqlalchemy 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy import MetaData, Table, Column
from sqlalchemy.orm import Session
from table_customer import Customer


class Database():
    """Handler of Customer table in database
    """

    engine = db.create_engine("postgresql://postgres:Pa$$w0rd@localhost:5432/test")

    def __init__(self):
        self.connection = self.engine.connect()
        print("DB instance create")

    
    def get_table(self, query):
        """returns an entire table
        :param query: Name table
        :type query: str
        """
        fetchQuery = self.connection.execute(f"SELECT * FROM {query}")
        for data in fetchQuery.fetchall():
            print(data)

    