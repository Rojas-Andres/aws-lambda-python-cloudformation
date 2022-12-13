from config.config import Settings
from sqlalchemy import create_engine
import sqlalchemy


class DataBase:
    def __init__(self):
        self.engine = create_engine(Settings().DATABASE_URL)
        self.metadata = sqlalchemy.MetaData()
        self.connection = self.engine.connect()
        self.user = sqlalchemy.Table(
            "usuarios", self.metadata, autoload=True, autoload_with=self.engine
        )

    def get_users(self):
        query = sqlalchemy.select([self.user])
        result = self.connection.execute(query)
        return result.fetchall()
