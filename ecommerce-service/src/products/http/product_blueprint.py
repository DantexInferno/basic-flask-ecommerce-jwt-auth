from flask import Blueprint, request, session

from src.validate_field.validate_schema import validate_schema_flask, SUCCESS_CODE, FAIL_CODE

from src.products.http.validation import product_validation_fields

from src.auth.auth import token_required, only_seller

def create_products_blueprint(manage_product_usecase):

    blueprint = Blueprint("products", __name__)


    @blueprint.route("/products", methods = ["GET"])
    @token_required
    def get_products():

        products = manage_product_usecase.get_products()

        products_dict = [product.serialize() for product in products]
        
        data = products_dict
        code = SUCCESS_CODE
        message = "Products obtained succesfully"
        http_code = 200

        response = {
            "code": code,
            "message": message,
            "data": data,
        }
        
        return response, http_code


    @blueprint.route("/products", methods = ["POST"])
    @validate_schema_flask(product_validation_fields.PRODUCT_CREATION_VALIDATION_FIELDS)
    @token_required
    @only_seller
    def create_product():

        body = request.get_json()

        try:
            product = manage_product_usecase.create_product(body)
            data = product.serialize()
            code = SUCCESS_CODE
            message = "Product created succesfully"
            http_code = 201

        except ValueError as e:
            data = None
            code = FAIL_CODE
            message = str(e)
            http_code = 400

        response = {
            "code": code,
            "message": message,
        }

        if data:
            response["data"] = data

        return response, http_code

    @blueprint.route("/products/<string:product_id>", methods = ["GET"])
    @token_required
    def get_product(product_id):

        product = manage_product_usecase.get_product(product_id)

        if product:
            data = product.serialize()
            code = SUCCESS_CODE
            message = "Product obtained succesfully"
            http_code = 200

        else:
            data = None
            code = FAIL_CODE
            message = f"Product of ID {product_id} does not exist."
            http_code = 404

        response = {
            "code": code,
            "message": message,
        }

        if data:
            response["data"] = data
        
        return response, http_code

    @blueprint.route("/products/<string:product_id>", methods = ["PUT"])
    @validate_schema_flask(product_validation_fields.PRODUCT_UPDATE_VALIDATION_FIELDS)
    @token_required
    @only_seller
    def update_product(product_id):

        body = request.get_json()

        try:
            product = manage_product_usecase.update_product(product_id, body)
            data = product.serialize()
            message = "Product updated succesfully"
            code = SUCCESS_CODE
            http_code = 200

        except ValueError as e:
            data = None
            code = FAIL_CODE
            message = str(e)
            http_code = 400

        response = {
            "code": code,
            "message": message,
        }

        if data:
            response["data"] = data

        return response, http_code
        

    @blueprint.route("/products/<string:product_id>", methods = ["DELETE"])
    @token_required
    @only_seller
    def delete_product(product_id):

        try:
            manage_product_usecase.delete_product(product_id)
            code = SUCCESS_CODE
            message = f"Product of ID {product_id} deleted succesfully."
            http_code = 200

        except ValueError as e:
            code = FAIL_CODE
            message = str(e)
            http_code = 400

        response = {
            "code": code,
            "message": message,
        }

        return response, http_code
    
    return blueprint

