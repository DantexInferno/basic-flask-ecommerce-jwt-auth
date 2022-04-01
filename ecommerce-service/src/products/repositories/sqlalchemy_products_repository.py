from sqlalchemy import Table, Column, Integer, String, ForeignKey, TIMESTAMP
from src.products.entities.product import Product
from src.sellers.entities.seller import Seller


class SQLAlchemyProductsRepository():

    def __init__(self, sqlalchemy_client, test = False):

        self.client = sqlalchemy_client
        self.session_factory = sqlalchemy_client.session_factory
        self.test = test

        table_name = "Products"

        if test:
            table_name += "_test"

        self.products_table = Table(
            table_name,
            sqlalchemy_client.mapper_registry.metadata,
            Column("id", Integer, primary_key = True),
            Column("name", String(255)),
            Column("description", String(50)),
            Column("quantity", Integer),
            Column("sku", String(30)),
            Column("seller_id", Integer, ForeignKey('Sellers.id')),
        )

        sqlalchemy_client.mapper_registry.map_imperatively(Product, self.products_table)

    def get_products(self):
        
        with self.session_factory() as session:
            
            products = session.query(Product).all()
            return products

    def get_product_by_sku(self, sku):
        with self.session_factory() as session:

            product = session.query(Product).filter_by(sku = sku).first()
            return product


    def create_product(self, product):

        with self.session_factory() as session:

            session.add(product)
            session.commit()

            return product
    
    def get_product(self, id):
        
        with self.session_factory() as session:

            product = session.query(Product).filter_by(id = id).first()
            return product

    def update_product(self, id, fields):
        
        with self.session_factory() as session:

            session.query(Product).filter_by(id = id).update(fields)
            session.commit()
            
            product = session.query(Product).filter_by(id = id).first()
            return product

    def hard_delete_product(self, id):

        with self.session_factory() as session:

            product = session.query(Product).get(id)
            session.delete(product)
            session.commit()

    def hard_delete_all_products(self):

        if self.test:

            with self.session_factory() as session:
                
                session.query(Product).delete()
                session.commit()
    

    def drop_products_table(self):

        if self.test:
            self.client.drop_table(self.products_table)

    def get_seller_id(self, id):
        
        with self.session_factory() as session:

            product = session.query(Seller).filter_by(user_seller_id = id).first()
            return product