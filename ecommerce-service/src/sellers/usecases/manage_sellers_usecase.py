from src.sellers.entities.seller import Seller

class ManageSellersUsecase:

    def __init__(self, sellers_repository):
        self.sellers_repository = sellers_repository

    def get_sellers(self):

        return self.sellers_repository.get_sellers()

    def create_seller(self, data):


        seller = Seller.from_dict(data)
        seller = self.sellers_repository.create_seller(seller)

        return seller

    def get_seller(self, seller_id):

        return self.sellers_repository.get_seller(seller_id)

    def update_seller(self, seller_id, data):

        seller = self.get_seller(seller_id)

        if seller:

            seller = self.sellers_repository.update_seller(seller_id, data)

            return seller

        else:
            raise ValueError(f"Seller of ID {seller_id} doesn't exist.")

    def delete_seller(self, seller_id):

        seller = self.get_seller(seller_id)

        if seller:

            seller = self.sellers_repository.hard_delete_seller(seller_id)

        else:
            raise ValueError(f"seller of ID {seller_id} doesn't exist or is already deleted.")
