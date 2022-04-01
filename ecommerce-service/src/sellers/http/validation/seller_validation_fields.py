SELLER_CREATION_VALIDATION_FIELDS = {
  "name": {
    "required": True,
    "type": "string"
  },
  "description": {
    "required": True,
    "type": "string"
  },
  "user_seller_id": {
    "required": True,
    "type": "integer"
  },
  "warehouse": {
    "required": True,
    "type": "string"
  }
}


SELLER_UPDATE_VALIDATION_FIELDS = {
  "name": {
    "required": False,
    "type": "string"
  },
  "description": {
    "required": False,
    "type": "string"
  },
  "user_seller_id": {
    "required": False,
    "type": "integer"
  },
  "warehouse": {
    "required": False,
    "type": "string"
  }
}