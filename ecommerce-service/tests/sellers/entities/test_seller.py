from src.sellers.entities.seller import Seller

class TestSeller:

    def test_to_dict(self):

        id = "1"
        name = "test"
        description = "test@test.com"
        user_seller_id = 1
        warehouse = "test warehouse"

        seller = Seller(id, name, description, user_seller_id, warehouse)


        dict = seller.to_dict()

        assert dict["id"] == id
        assert dict["name"] == name
        assert dict["description"] == description
        assert dict["user_seller_id"] == user_seller_id
        assert dict["warehouse"] == warehouse

    def test_serialize(self):


        id = "1"
        name = "test"
        description = "test"
        user_seller_id = 1
        warehouse = "test warehouse"

        seller = Seller(id, name, description, user_seller_id, warehouse)

        
        data = seller.serialize()

        assert data["id"] == id
        assert data["name"] == name
        assert data["description"] == description
        assert data["user_seller_id"] == user_seller_id
        assert data["warehouse"] == warehouse

    def test_from_dict(self):


        dict = {
            "id": "2",
            "name": "test",
            "description": "test",
            "user_seller_id": 1,
            "warehouse": "tes warehouse",
        }


        seller = Seller.from_dict(dict)

        assert seller.id == dict["id"]
        assert seller.name == dict["name"]
        assert seller.description == dict["description"]
        assert seller.user_seller_id == dict["user_seller_id"]
        assert seller.warehouse == dict["warehouse"] 
