from lib_users.config import Settings
from sqlalchemy import create_engine
import sqlalchemy
from sqlalchemy.orm import Session
import pandas as pd
from lib_users.querys import Query
import io


class DataBase:
    def __init__(self):
        self.engine = create_engine(Settings().DATABASE_URL)
        self.metadata = sqlalchemy.MetaData()
        self.connection = self.engine.connect()
        self.user = sqlalchemy.Table(
            "users", self.metadata, autoload=True, autoload_with=self.engine
        )

    def get_users(self):
        query = sqlalchemy.select([self.user])
        result = self.connection.execute(query)
        return result.fetchall()

    def create_user(self, user=dict):
        session = Session(self.engine, future=True)
        query = (
            self.user.insert()
            .values(user)
            .returning(
                self.user.c.id,
                self.user.c.name,
                self.user.c.last_name,
                self.user.c.city,
                self.user.c.email,
                self.user.c.password,
            )
        )
        result = session.execute(query)
        session.commit()
        session.close()
        return dict(result.fetchone())

    def get_user_by_id(self, id):
        query = sqlalchemy.select([self.user]).where(self.user.c.id == id)
        result = self.connection.execute(query)
        return result.fetchone()

    def update_user(self, id, user):
        session = Session(self.engine, future=True)
        query = (
            self.user.update()
            .where(self.user.c.id == id)
            .values(user)
            .returning(
                self.user.c.id,
                self.user.c.name,
                self.user.c.last_name,
                self.user.c.city,
            )
        )
        result = session.execute(query)
        session.commit()
        session.close()
        return dict(result.fetchone())

    def delete_user_by_id(self, id):
        session = Session(self.engine, future=True)
        query = self.user.delete().where(self.user.c.id == id)
        result = session.execute(query)
        session.commit()
        session.close()

    def get_user_by_email(self, email):
        query = sqlalchemy.select([self.user]).where(self.user.c.email == email)
        result = self.connection.execute(query).fetchone()
        return dict(result) if result else None
    
    def get_user_create_today(self):
        df = pd.read_sql(Query().get_users_create_today(), self.connection)
        with io.BytesIO() as output:
            with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
                df.to_excel(writer, sheet_name='Sheet1', index=False)
            data = output.getvalue()
        return data