from lib_notification.config import Settings
from sqlalchemy import create_engine
import sqlalchemy
from sqlalchemy.orm import Session
from lib_notification.querys import Query

class DataBase:
    def __init__(self):
        self.engine = create_engine(Settings().DATABASE_URL)
        self.metadata = sqlalchemy.MetaData()
        self.connection = self.engine.connect()
        self.user = sqlalchemy.Table(
            "users", self.metadata, autoload=True, autoload_with=self.engine
        )
    
    def get_users_create_today(self):
        result = self.connection.execute(Query().get_users_create_today())
        return result.fetchall()
        