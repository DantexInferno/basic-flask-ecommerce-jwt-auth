from sqlalchemy import Table, Column, Integer, String, ForeignKey, TIMESTAMP
from src.orders.entities.order import Order
from src.products.repositories.sqlalchemy_products_repository import SQLAlchemyProductsRepository
from src.products.entities.product import Product


class SQLAlchemyOrdersRepository():

    def __init__(self, sqlalchemy_client, test = False):

        self.client = sqlalchemy_client
        self.session_factory = sqlalchemy_client.session_factory
        self.test = test

        table_name = "Orders"

        if test:
            table_name += "_test"

        self.orders_table = Table(
            table_name,
            sqlalchemy_client.mapper_registry.metadata,
            Column("id", Integer, primary_key = True),
            Column("product_sku", String(30)),
            Column("product_name", String(255)),
            Column("quantity", Integer),
            Column("seller_name", String(100)),
            Column("seller_warehouse", String(255)),
            Column("marketplace_user_name", String(50)),
            Column("marketplace_user_adress", String(255)),
            Column("status", String(20)),
        )

        sqlalchemy_client.mapper_registry.map_imperatively(Order, self.orders_table)

    def get_orders(self):
        
        with self.session_factory() as session:
            
            orders = session.query(Order).filter_by(status="created").all()
            return orders


    def create_order(self, order):

        with self.session_factory() as session:

            session.add(order)
            session.commit()

            return order
    
    def get_order(self, id):
        
        with self.session_factory() as session:

            order = session.query(Order).filter_by(id = id).first()
            return order

    def update_order(self, id, fields):
        
        with self.session_factory() as session:

            session.query(Order).filter_by(id = id).update(fields)
            session.commit()
            
            order = session.query(Order).filter_by(id = id).first()
            return order

    def hard_delete_order(self, id):

        with self.session_factory() as session:

            order = session.query(Order).get(id)
            session.delete(order)
            session.commit()

    def hard_delete_all_orders(self):

        if self.test:

            with self.session_factory() as session:
                
                session.query(Order).delete()
                session.commit()
    

    def drop_orders_table(self):

        if self.test:
            self.client.drop_table(self.orders_table)

    def product_by_sku(self, sku):
        with self.session_factory() as session:

            product = session.query(Product).filter_by(sku = sku).first()
            return product


    def update_product(self, id, fields):
        
        with self.session_factory() as session:

            session.query(Product).filter_by(id = id).update(fields)
            session.commit()
            
            product = session.query(Product).filter_by(id = id).first()
            return product