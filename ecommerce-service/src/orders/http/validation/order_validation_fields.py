ORDER_CREATION_VALIDATION_FIELDS = {
  "product_sku": {
    "required": True,
    "type": "string"
  },
  "product_name": {
    "required": True,
    "type": "string"
  },
  "quantity": {
    "required": True,
    "type": "integer"
  },
  "seller_name": {
    "required": True,
    "type": "string"
  },
  "seller_warehouse": {
    "required": True,
    "type": "string"
  },
  "marketplace_user_name": {
    "required": True,
    "type": "string"
  },
  "marketplace_user_adress": {
    "required": True,
    "type": "string"
  }
}


ORDER_UPDATE_VALIDATION_FIELDS = {
  "product_sku": {
    "required": False,
    "type": "string"
  },
  "product_name": {
    "required": False,
    "type": "string"
  },
  "quantity": {
    "required": False,
    "type": "integer"
  },
  "seller_name": {
    "required": False,
    "type": "string"
  },
  "seller_warehouse": {
    "required": False,
    "type": "string"
  },
  "marketplace_user_name": {
    "required": False,
    "type": "string"
  },
  "marketplace_user_adress": {
    "required": False,
    "type": "string"
  },
  "status": {
    "required": False,
    "type": "string"
  }
}