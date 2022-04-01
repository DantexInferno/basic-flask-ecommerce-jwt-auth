PRODUCT_CREATION_VALIDATION_FIELDS = {
  "name": {
    "required": True,
    "type": "string"
  },
  "description": {
    "required": True,
    "type": "string"
  },
  "quantity": {
    "required": True,
    "type": "integer"
  },
  "sku": {
    "required": True,
    "type": "string"
  }
}


PRODUCT_UPDATE_VALIDATION_FIELDS = {
  "name": {
    "required": False,
    "type": "string"
  },
  "description": {
    "required": False,
    "type": "string"
  },
  "quantity": {
    "required": False,
    "type": "integer"
  },
  "sku": {
    "required": False,
    "type": "string"
  }
}