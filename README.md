###Flask Ecommerce with jwt authentication

this is a simple project of a ecommerce with jwt authentication

in the User module you can register 3 types of user when gonna sign up :

- Marketplace Administrator
- Seller User
- Marketplace User

there only can register 1 user with the role of Marketplace Administrator the others can be "Seller User" or "Marketplace User".


the Seller User need to be registered in other table to determinate that is a seller by the Marketplace Administrator then it can register products
the Marketplace Administrator is the only who can create, edit, consult and delete sellers



this is the template to register a user, this template can be used to update the user

POST http://localhost:8000/users
Content-Type: application/json

{   
    "name": "xxxxx",
    "email": "xxxxxx@xxxxxx.com",
    "password": "test123",
    "role": "Marketplace Administrator",
    "shipping_address": "xxxxxxxxx"
}

this is the template to register sellers

POST http://localhost:8000/sellers
Content-Type: application/json

{
    "name": "xxxxxxxx",
    "description": "xxxxxxx",
    "user_seller_id": 1,
    "warehouse": "xxxxxx"
}


this is the template to register products

POST http://localhost:8000/products
Content-Type: application/json



{
    "name": "smartphone xiaomi",
    "description": "smartphone xiaomi note 8",
    "quantity": 10,
    "sku": "7854236985",
    "seller_id": 1
}

this is the templare to create orders

POST http://localhost:8000/orders
Content-Type: application/json

{
    "product_sku": "7854236985",
    "product_name": "smartphone xiaomi",
    "quantity": 2,
    "seller_name": "walmart",
    "seller_warehouse": "nord 122",
    "marketplace_user_name": "chris",
    "marketplace_user_adress": "south 56565"
}


### TO RUN the APP
change the name of the file .env.example to .env the same into the folder ecommerce-service/Docker/app

1. then open a terminal in the root location of the project and execute "docker-compose build" 

2. when the process finish execute "docker-compose up" then when this process have finished in the terminal press "CRTL + C" when all the containers stopped execute again "docker-compose up"

this is because the first time the mysql container take  longer to execute than the ecommerce container and this not reconize it.