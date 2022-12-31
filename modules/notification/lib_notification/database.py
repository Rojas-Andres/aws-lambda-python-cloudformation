from lib_notification.config import Settings
from sqlalchemy import create_engine
import sqlalchemy
from sqlalchemy.orm import Session
from lib_notification.querys import Query
import pandas as pd
import io

class DataBase:
    def __init__(self):
        self.engine = create_engine(Settings().DATABASE_URL)
        self.metadata = sqlalchemy.MetaData()
        self.connection = self.engine.connect()
        self.user = sqlalchemy.Table(
            "users", self.metadata, autoload=True, autoload_with=self.engine
        )
    
    def get_user_create_today(self):
        df = pd.read_sql(Query().get_users_create_today(), self.connection)
        with io.BytesIO() as output:
            with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
                df.to_excel(writer, sheet_name='Sheet1', index=False)
            data = output.getvalue()
        return data