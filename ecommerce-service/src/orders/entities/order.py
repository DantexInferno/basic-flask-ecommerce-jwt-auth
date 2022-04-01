class Order():
  
  def __init__(self, id, product_sku, product_name, quantity, seller_name,
    seller_warehouse, marketplace_user_name, marketplace_user_adress, status):
    self.id = id
    self.product_sku = product_sku
    self.product_name = product_name
    self.quantity = quantity
    self.seller_name = seller_name
    self.seller_warehouse = seller_warehouse
    self.marketplace_user_name = marketplace_user_name
    self.marketplace_user_adress = marketplace_user_adress
    self.status = status


  def to_dict(self):

    return {
      "id": self.id, 
      "product_sku": self.product_sku,
      "product_name": self.product_name,
      "quantity": self.quantity,
      "seller_name": self.seller_name,
      "seller_warehouse": self.seller_warehouse,
      "marketplace_user_name": self.marketplace_user_name,
      "marketplace_user_adress": self.marketplace_user_adress,
      "status": self.status
      }

  def serialize(self):
  
        data = self.to_dict()  

        return data


  @classmethod
  def from_dict(cls, dict):

      id = dict.get("id")
      product_sku = dict.get("product_sku")
      product_name = dict.get("product_name")
      quantity = dict.get("quantity")
      
      seller_name = dict.get("seller_name")
      seller_warehouse = dict.get("seller_warehouse")
      marketplace_user_name = dict.get("marketplace_user_name")
      marketplace_user_adress = dict.get("marketplace_user_adress")
      status = dict.get("status")

      return Order(id, product_sku, product_name, quantity, seller_name, 
        seller_warehouse, marketplace_user_name, marketplace_user_adress, status)

