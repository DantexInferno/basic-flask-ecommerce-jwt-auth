class User():

  def __init__(self, id, name, email, password, role, shipping_address, public_id):
    self.id = id
    self.name = name
    self.email = email
    self.password = password
    self.role = role
    self.shipping_address = shipping_address
    self.public_id = public_id


  def to_dict(self):

    return {
      "id": self.id,
      "name": self.name,
      "email": self.email,
      "password": self.password,
      "role": self.role,
      "shipping_address": self.shipping_address,
      "public_id": self.public_id
      }

  def serialize(self):
  
        data = self.to_dict()  

        return data


  @classmethod
  def from_dict(cls, dict):

      id = dict.get("id")
      name = dict.get("name")
      email = dict.get("email")
      password = dict.get("password")
      role = dict.get("role")
      shipping_address = dict.get("shipping_address")
      public_id = dict.get("public_id")

      return User(id, name, email, password, role, shipping_address, public_id)

