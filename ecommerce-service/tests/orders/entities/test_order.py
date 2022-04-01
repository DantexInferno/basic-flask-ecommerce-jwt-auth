from datetime import datetime

from src.orders.entities.order import Order

class TestOrder:

    def test_to_dict(self):

        id = "1"
        product_sku = "test"
        product_name = "test@test.com"
        quantity = 10
        seller_name = "test seller_name"
        seller_warehouse = "nort 1"
        marketplace_user_name = "test user"
        marketplace_user_adress = "nort 2"
        status = "created"

        order = Order(id, product_sku, product_name, quantity, seller_name, seller_warehouse, marketplace_user_name, marketplace_user_adress, status)


        dict = order.to_dict()

        assert dict["id"] == id
        assert dict["product_sku"] == product_sku
        assert dict["product_name"] == product_name
        assert dict["quantity"] == quantity
        assert dict["seller_name"] == seller_name
        assert dict["seller_warehouse"] == seller_warehouse
        assert dict["marketplace_user_name"] == marketplace_user_name
        assert dict["marketplace_user_adress"] == marketplace_user_adress 
        assert dict["status"] == status

    def test_serialize(self):

        id = "1"
        product_sku = "test"
        product_name = "test"
        quantity = 10
        seller_name = "test seller_name"
        seller_warehouse = "nort 1"
        marketplace_user_name = "test user"
        marketplace_user_adress = "nort 2"
        status = "created"

        order = Order(id, product_sku, product_name, quantity, seller_name, seller_warehouse,  marketplace_user_name, marketplace_user_adress, status)

        
        data = order.serialize()

        assert data["id"] == id
        assert data["product_sku"] == product_sku
        assert data["product_name"] == product_name
        assert data["quantity"] == quantity
        assert data["seller_name"] == seller_name
        assert data["seller_warehouse"] == seller_warehouse
        assert data["marketplace_user_name"] == marketplace_user_name
        assert data["marketplace_user_adress"] == marketplace_user_adress
        assert data["status"] == status

    def test_from_dict(self):


        dict = {
            "id": "2",
            "product_sku": "test",
            "product_name": "test",
            "quantity": 10,
            "seller_name": "tes seller_name",
            "seller_warehouse": "nort 1",
            "marketplace_user_name": "test user",
            "marketplace_user_adress": "nort 2",
            "status": "created"
        }


        order = Order.from_dict(dict)

        assert order.id == dict["id"]
        assert order.product_sku == dict["product_sku"]
        assert order.product_name == dict["product_name"]
        assert order.quantity == dict["quantity"]
        assert order.seller_name == dict["seller_name"] 
        assert order.seller_warehouse == dict["seller_warehouse"]
        assert order.marketplace_user_name == dict["marketplace_user_name"]
        assert order.marketplace_user_adress == dict["marketplace_user_adress"] 
        assert order.status == dict["status"]
        