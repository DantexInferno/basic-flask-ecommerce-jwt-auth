import pytest

from datetime import datetime
from unittest.mock import Mock

from src.products.entities.product import Product
from src.products.usecases.manage_products_usecase import ManageProductsUsecase
from werkzeug.security import check_password_hash



@pytest.fixture
def repository_mock():
    return Mock()

@pytest.fixture
def manage_products_usecase(repository_mock):
    return ManageProductsUsecase(repository_mock)

class TestManageProductsUsecase:

    def test_get_products(self, manage_products_usecase):


        mock_products = [
            Product(1, "playstation 1", " old console",  5, "4554456565", 1),
            Product(2, "playstation 2", " old console",  5, "4554456554", 2),
            Product(3, "playstation 3", " old console",  5, "4554478955", 3),
        ]

        manage_products_usecase.products_repository.get_products.return_value = mock_products

        products = manage_products_usecase.get_products()
        
        assert len(products) == len(mock_products)

    def test_create_product(self, manage_products_usecase):

        mock_id = 25

        data = {
            "name": "test-name",
            "description": "test-description",
            "quantity": 10,
            "sku": "test sku",
            "seller_id": 1
        };
        
        mock_product = Product.from_dict(data)
        mock_product.id = mock_id
        
        manage_products_usecase.products_repository.create_product.return_value = mock_product
        
        product = manage_products_usecase.create_product(data);
        
        assert product.id == mock_id
        assert product.name == data["name"]
        assert product.description == data["description"]
        assert product.quantity ==  data["quantity"]
        assert product.sku == data["sku"]
        assert product.seller_id == data["seller_id"]