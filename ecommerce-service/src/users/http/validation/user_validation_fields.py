USER_CREATION_VALIDATION_FIELDS = {
  "name": {
    "required": True,
    "type": "string"
  },
  "email": {
    "required": True,
    "type": "string"
  },
  "password": {
    "required": True,
    "type": "string"
  },
  "role": {
    "required": True,
    "type": "string"
  },
  "shipping_address":{
    "required": False,
    "type": "string"
  }
}


USER_UPDATE_VALIDATION_FIELDS = {
  "name": {
    "required": False,
    "type": "string"
  },
  "email": {
    "required": False,
    "type": "string"
  },
  "password": {
    "required": False,
    "type": "string"
  },
  "role": {
    "required": False,
    "type": "string"
  },
  "shipping_address":{
    "required": False,
    "type": "string"
  }
}


USER_LOGIN_VALIDATION_FIELDS = {
  "email": {
    "required": True,
    "type": "string"
  },
  "password": {
    "required": False,
    "type": "string"
  },
}