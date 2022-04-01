import pytest

from datetime import datetime
from unittest.mock import Mock

from src.sellers.entities.seller import Seller
from src.sellers.usecases.manage_sellers_usecase import ManageSellersUsecase
from werkzeug.security import check_password_hash



@pytest.fixture
def repository_mock():
    return Mock()

@pytest.fixture
def manage_sellers_usecase(repository_mock):
    return ManageSellersUsecase(repository_mock)

class TestManageSellersUsecase:

    def test_get_sellers(self, manage_sellers_usecase):


        mock_sellers = [
            Seller(1, "seller1", "seller number 1", 1, "warehouse seller"),
            Seller(2, "seller2", "seller number 2", 2, "warehouse seller"),
            Seller(3, "seller3", "seller number 3", 3, "warehouse seller"),
        ]

        manage_sellers_usecase.sellers_repository.get_sellers.return_value = mock_sellers

        sellers = manage_sellers_usecase.get_sellers()
        
        assert len(sellers) == len(mock_sellers)

    def test_create_seller(self, manage_sellers_usecase):

        mock_id = 25

        data = {
            "name": "test-name",
            "description": "test-description",
            "user_seller_id": 1,
            "warehouse": "test warehouse",
        };
        
        mock_seller = Seller.from_dict(data)
        mock_seller.id = mock_id
        
        manage_sellers_usecase.sellers_repository.create_seller.return_value = mock_seller
        
        seller = manage_sellers_usecase.create_seller(data);

        
        assert seller.id == mock_id
        assert seller.name == data["name"]
        assert seller.description == data["description"]
        assert seller.user_seller_id ==  data["user_seller_id"]
        assert seller.warehouse == data["warehouse"]
