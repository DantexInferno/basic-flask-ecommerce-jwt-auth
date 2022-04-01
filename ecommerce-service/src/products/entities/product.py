class Product():
  
  def __init__(self, id, name, description, quantity, sku, seller_id):
    self.id = id
    self.name = name
    self.description = description
    self.quantity = quantity
    self.sku = sku
    self.seller_id = seller_id


  def to_dict(self):

    return {
      "id": self.id, 
      "name": self.name,
      "description": self.description,
      "quantity": self.quantity,
      "sku": self.sku,
      "seller_id": self.seller_id
      }

  def serialize(self):
  
        data = self.to_dict()  

        return data


  @classmethod
  def from_dict(cls, dict):

      id = dict.get("id")
      name = dict.get("name")
      description = dict.get("description")
      quantity = dict.get("quantity")
      sku = dict.get("sku")
      seller_id = dict.get("seller_id")

      return Product(id, name, description, quantity, sku, seller_id)

