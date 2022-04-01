from src.products.entities.product import Product
from flask import g

class ManageProductsUsecase:

    def __init__(self, products_repository):
        self.products_repository = products_repository


    def get_products(self):

        return self.products_repository.get_products()


    def get_product_by_sku(self, sku):
        
        return self.products_repository.get_product_by_sku(sku)


    def create_product(self, data):

        if g.user.role == "Seller User":
            seller = self.products_repository.get_seller_id(g.user.id)
            data["seller_id"] = seller.id

        product = Product.from_dict(data)
        product = self.products_repository.create_product(product)

        return product


    def get_product(self, product_id):

        return self.products_repository.get_product(product_id)


    def update_product(self, product_id, data):

        product = self.get_product(product_id)

        if product:

            product = self.products_repository.update_product(product_id, data)

            return product

        else:
            raise ValueError(f"Product of ID {product_id} doesn't exist.")

    def delete_product(self, product_id):

        product = self.get_product(product_id)

        if product:

            
            product = self.products_repository.hard_delete_product(product_id)

        else:
            raise ValueError(f"Product of ID {product_id} doesn't exist or is already deleted.")
