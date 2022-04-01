from datetime import datetime

from src.products.entities.product import Product

class TestProduct:

    def test_to_dict(self):

        id = "1"
        name = "xbox"
        description = "test@test.com"
        quantity = 24
        sku = "test sku"
        seller_id = 1

        product = Product(id, name, description, quantity, sku, seller_id)


        dict = product.to_dict()

        assert dict["id"] == id
        assert dict["name"] == name
        assert dict["description"] == description
        assert dict["quantity"] == quantity
        assert dict["sku"] == sku
        assert dict["seller_id"] == seller_id

    def test_serialize(self):

        id = "1"
        name = "xbox"
        description = "test"
        quantity = 24
        sku = "test sku"
        seller_id = 1

        product = Product(id, name, description, quantity, sku, seller_id)

        
        data = product.serialize()

        assert data["id"] == id
        assert data["name"] == name
        assert data["description"] == description
        assert data["quantity"] == quantity
        assert data["sku"] == sku
        assert data["seller_id"] == seller_id

    def test_from_dict(self):


        dict = {
            "id": "2",
            "name": "xbox",
            "description": "test",
            "quantity": 24,
            "sku": "tes sku",
            "seller_id": 1
        }


        product = Product.from_dict(dict)

        assert product.id == dict["id"]
        assert product.name == dict["name"]
        assert product.description == dict["description"]
        assert product.quantity == dict["quantity"]
        assert product.sku == dict["sku"] 
        assert product.seller_id == dict["seller_id"]