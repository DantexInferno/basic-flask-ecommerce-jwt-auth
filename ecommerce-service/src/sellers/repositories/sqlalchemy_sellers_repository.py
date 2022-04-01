from sqlalchemy import Table, Column, Integer, String, ForeignKey, TIMESTAMP
from src.sellers.entities.seller import Seller

class SQLAlchemySellersRepository():

    def __init__(self, sqlalchemy_client, test = False):

        self.client = sqlalchemy_client
        self.session_factory = sqlalchemy_client.session_factory
        self.test = test

        table_name = "Sellers"

        if test:
            table_name += "_test"

        self.sellers_table = Table(
            table_name,
            sqlalchemy_client.mapper_registry.metadata,
            Column("id", Integer, primary_key = True),
            Column("name", String(100)),
            Column("description", String(50)),
            Column("user_seller_id", Integer, ForeignKey('Users.id')),
            Column("warehouse", String(255)),
        )

        sqlalchemy_client.mapper_registry.map_imperatively(Seller, self.sellers_table)

    def get_sellers(self):
        
        with self.session_factory() as session:
            
            sellers = session.query(Seller).all()
            return sellers


    def create_seller(self, seller):

        with self.session_factory() as session:

            session.add(seller)
            session.commit()

            return seller
    
    def get_seller(self, id):
        
        with self.session_factory() as session:

            seller = session.query(Seller).filter_by(id = id).first()
            return seller

    def update_seller(self, id, fields):
        
        with self.session_factory() as session:

            session.query(Seller).filter_by(id = id).update(fields)
            session.commit()
            
            seller = session.query(Seller).filter_by(id = id).first()
            return seller


    def hard_delete_seller(self, id):

        with self.session_factory() as session:

            seller = session.query(Seller).get(id)
            session.delete(seller)
            session.commit()

    def hard_delete_all_sellers(self):

        if self.test:

            with self.session_factory() as session:
                
                session.query(Seller).delete()
                session.commit()
    

    def drop_sellers_table(self):

        if self.test:
            self.client.drop_table(self.sellers_table)