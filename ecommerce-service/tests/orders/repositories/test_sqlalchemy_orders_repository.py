import pytest

from src.frameworks.db.sqlalchemy import SQLAlchemyClient
from src.orders.entities.order import Order
from src.orders.repositories.sqlalchemy_orders_repository import SQLAlchemyOrdersRepository


@pytest.fixture(scope = "session")
def client():
    return SQLAlchemyClient()

@pytest.fixture(scope = "session")
def repository(client):
    return SQLAlchemyOrdersRepository(client, test = True)

@pytest.fixture(autouse = True)
def before_each(repository):
    
    repository.hard_delete_all_orders()
    yield

@pytest.fixture(autouse = True, scope = "session")
def before_and_after_all(client, repository):

    client.create_tables()
    
    yield
    
    repository.drop_orders_table()
    client.dispose_mapper()

class TestSqlAlchemyOrdersRepository:

    def test_create_and_get_order(self, repository):


        product_sku = "test"
        product_name = "test@test.com"
        quantity = 10
        seller_name = "test seller_name"
        seller_warehouse = "nort 1"
        marketplace_user_name = "test user"
        marketplace_user_adress = "nort 2"
        status = "created"
        
        order = Order(None, product_sku, product_name, quantity, seller_name, seller_warehouse, marketplace_user_name, marketplace_user_adress, status)
        order = repository.create_order(order)

        print("Created order:", order.to_dict())

        saved_order = repository.get_order(order.id)

        orders = repository.get_orders()
        for order in orders:
            print(order)

        print(saved_order)
        
        print("Saved order:", saved_order.to_dict())


        assert order.id == saved_order.id
        assert order.product_sku == saved_order.product_sku
        assert order.product_name == saved_order.product_name
        assert order.quantity == saved_order.quantity
        assert order.seller_name == saved_order.seller_name
        assert order.seller_warehouse == saved_order.seller_warehouse
        assert order.marketplace_user_name == saved_order.marketplace_user_name
        assert order.marketplace_user_adress == saved_order.marketplace_user_adress
        assert order.status == saved_order.status

    def test_delete_order(self, repository):


        product_sku = "test"
        product_name = "test@test.com"
        quantity = 10
        seller_name = "test seller_name"
        seller_warehouse = "nort 1"
        marketplace_user_name = "test user"
        marketplace_user_adress = "nort 2"
        status = "created"
        
        

        ids = []

        for i in range(0, 3):
            order = Order(None, product_sku, product_name, quantity, seller_name, seller_warehouse, marketplace_user_name, marketplace_user_adress, status)
            order = repository.create_order(order)
            ids.append(order.id)

        print("Added orders:", ids)


        deleted_id = ids.pop(1)
        print(deleted_id)
        repository.hard_delete_order(deleted_id)

        print("Deleted order:", deleted_id)

        # Obtener las IDs de los usuarios restantes.

        orders = repository.get_orders()

        current_ids = []
        for order in orders:
            current_ids.append(order.id)

        print("Current orders:", current_ids)
        print("Expected orders:", ids)

        # Afirmar que las IDs restantes correspondan
        # a los recursos que no fueron eliminados.

        assert set(current_ids) == set(ids)
