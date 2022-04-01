class Seller():
  
  def __init__(self, id, name, description, user_seller_id, warehouse):
    self.id = id
    self.name = name
    self.description = description
    self.user_seller_id = user_seller_id
    self.warehouse = warehouse


  def to_dict(self):

    return {
      "id": self.id, 
      "name": self.name,
      "description": self.description,
      "user_seller_id": self.user_seller_id,
      "warehouse": self.warehouse
      }

  def serialize(self):
  
        data = self.to_dict()  

        return data


  @classmethod
  def from_dict(cls, dict):

      id = dict.get("id")
      name = dict.get("name")
      description = dict.get("description")
      user_seller_id = dict.get("user_seller_id")
      warehouse = dict.get("warehouse")

      return Seller(id, name, description, user_seller_id, warehouse)

