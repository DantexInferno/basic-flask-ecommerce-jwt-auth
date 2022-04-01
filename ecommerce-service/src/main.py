import sqlalchemy
from src.frameworks.db.sqlalchemy import SQLAlchemyClient
from src.frameworks.http.flask import create_flask_app


#USERS
from src.users.http.user_blueprint import create_users_blueprint
from src.users.repositories.sqlalchemy_users_repository import SQLAlchemyUsersRepository
from src.users.usecases.manage_users_usecase import ManageUsersUsecase

#PRODUCTS
from src.products.http.product_blueprint import create_products_blueprint
from src.products.repositories.sqlalchemy_products_repository import SQLAlchemyProductsRepository
from src.products.usecases.manage_products_usecase import ManageProductsUsecase

#SELLERS
from src.sellers.http.seller_blueprint import create_sellers_blueprint
from src.sellers.repositories.sqlalchemy_sellers_repository import SQLAlchemySellersRepository
from src.sellers.usecases.manage_sellers_usecase import ManageSellersUsecase

#ORDERS
from src.orders.http.order_blueprint import create_orders_blueprint
from src.orders.repositories.sqlalchemy_orders_repository import SQLAlchemyOrdersRepository
from src.orders.usecases.manage_orders_usecase import ManageOrdersUsecase


# Instanciar dependencias.

sqlalchemy_client = SQLAlchemyClient()
sqlalchemy_users_repository = SQLAlchemyUsersRepository(sqlalchemy_client)
sqlalchemy_products_repository = SQLAlchemyProductsRepository(sqlalchemy_client)
sqlalchemy_sellers_repository = SQLAlchemySellersRepository(sqlalchemy_client)
sqlalchemy_orders_repository = SQLAlchemyOrdersRepository(sqlalchemy_client)
sqlalchemy_client.create_tables()



manage_users_usecase = ManageUsersUsecase(sqlalchemy_users_repository)
manage_products_usecase = ManageProductsUsecase(sqlalchemy_products_repository)
manage_sellers_usecase = ManageSellersUsecase(sqlalchemy_sellers_repository)
manage_orders_usecase = ManageOrdersUsecase(sqlalchemy_orders_repository)

blueprints = [

    create_users_blueprint(manage_users_usecase),
    create_products_blueprint(manage_products_usecase),
    create_sellers_blueprint(manage_sellers_usecase),
    create_orders_blueprint(manage_orders_usecase)
]

# Crear aplicación HTTP con dependencias inyectadas.

app = create_flask_app(blueprints)