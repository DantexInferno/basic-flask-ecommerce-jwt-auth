import pytest

from datetime import datetime
from unittest.mock import Mock

from src.orders.entities.order import Order
from src.orders.usecases.manage_orders_usecase import ManageOrdersUsecase
from werkzeug.security import check_password_hash



@pytest.fixture
def repository_mock():
    return Mock()

@pytest.fixture
def manage_orders_usecase(repository_mock):
    return ManageOrdersUsecase(repository_mock)

class TestManageOrdersUsecase:

    def test_get_orders(self, manage_orders_usecase):


        mock_orders = [
            Order(1, "4525544547891", " playstation 1", 10, "Seller amazon", "nort 1", "jake", "nort 2", "created"),
            Order(2, "4525544547892", " playstation 2", 10, "Seller amazon", "nort 2", "jake", "nort 2", "created"),
            Order(3, "4525544547893", " playstation 3", 10, "Seller amazon", "nort 3", "jake", "nort 2", "created"),
        ]

        manage_orders_usecase.orders_repository.get_orders.return_value = mock_orders

        orders = manage_orders_usecase.get_orders()
        
        assert len(orders) == len(mock_orders)

    def test_create_order(self, manage_orders_usecase):

        mock_id = 25

        data = {
            "product_sku": "test",
            "product_name": "test",
            "quantity": 10,
            "seller_name": "tes seller_name",
            "seller_warehouse": "nort 1",
            "marketplace_user_name": "test user",
            "marketplace_user_adress": "nort 2",
            "status": "created"
        };
        
        mock_order = Order.from_dict(data)
        mock_order.id = mock_id
        
        manage_orders_usecase.orders_repository.create_order.return_value = mock_order
        
        order = manage_orders_usecase.create_order(data);

        
        assert order.product_sku == data["product_sku"]
        assert order.product_name == data["product_name"]
        assert order.quantity == data["quantity"]
        assert order.seller_name == data["seller_name"] 
        assert order.seller_warehouse == data["seller_warehouse"]
        assert order.marketplace_user_name == data["marketplace_user_name"]
        assert order.marketplace_user_adress == data["marketplace_user_adress"] 
        assert order.status == data["status"]