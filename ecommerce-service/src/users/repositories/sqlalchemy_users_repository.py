from enum import unique
from sqlalchemy import Table, Column, Integer, String, ForeignKey, TIMESTAMP
from src.users.entities.user import User

class SQLAlchemyUsersRepository():

    def __init__(self, sqlalchemy_client, test = False):

        self.client = sqlalchemy_client
        self.session_factory = sqlalchemy_client.session_factory
        self.test = test

        table_name = "Users"

        if test:
            table_name += "_test"

        self.users_table = Table(
            table_name,
            sqlalchemy_client.mapper_registry.metadata,
            Column("id", Integer, primary_key = True),
            Column("name", String(50)),
            Column("email", String(255)),
            Column("password", String(255)),
            Column("role", String(25)),
            Column("shipping_address", String(255)),
            Column("public_id", String(50), unique=True),
        )

        sqlalchemy_client.mapper_registry.map_imperatively(User, self.users_table)

    def get_users(self):
        
        with self.session_factory() as session:
            
            users = session.query(User).all()
            return users


    def create_user(self, user):

        with self.session_factory() as session:

            session.add(user)
            session.commit()

            return user
    
    def get_user(self, id):
        
        with self.session_factory() as session:

            user = session.query(User).filter_by(id = id).first()
            return user

    def update_user(self, id, fields):
        
        with self.session_factory() as session:

            session.query(User).filter_by(id = id).update(fields)
            session.commit()
            
            user = session.query(User).filter_by(id = id).first()
            return user

    def get_user_by_email(self, email):
        with self.session_factory() as session:

            user = session.query(User).filter_by(email = email).first()
            return user

    
    def hard_delete_user(self, id):

        with self.session_factory() as session:

            user = session.query(User).get(id)
            session.delete(user)
            session.commit()

    def hard_delete_all_users(self):

        if self.test:

            with self.session_factory() as session:
                
                session.query(User).delete()
                session.commit()
    
    def drop_users_table(self):

        if self.test:
            self.client.drop_table(self.users_table)